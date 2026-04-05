from __future__ import annotations

import os
import unittest
from unittest.mock import MagicMock, patch

from src.deepseek_client import chat_completion, simple_prompt


class DeepseekClientTests(unittest.TestCase):
    def test_chat_completion_requires_key(self) -> None:
        with patch.dict(os.environ, {}, clear=True):
            with self.assertRaises(ValueError) as ctx:
                chat_completion([{'role': 'user', 'content': 'hi'}])
            self.assertIn('DEEPSEEK_API_KEY', str(ctx.exception))

    @patch('src.deepseek_client.urllib.request.urlopen')
    def test_chat_completion_parses_choice(self, mock_urlopen: MagicMock) -> None:
        mock_inner = MagicMock()
        mock_inner.read.return_value = (
            b'{"choices":[{"message":{"content":"  hello  "}}],"usage":{}}'
        )
        mock_cm = MagicMock()
        mock_cm.__enter__.return_value = mock_inner
        mock_cm.__exit__.return_value = False
        mock_urlopen.return_value = mock_cm
        with patch.dict(os.environ, {'DEEPSEEK_API_KEY': 'test-key'}):
            text, raw = chat_completion([{'role': 'user', 'content': 'x'}])
        self.assertEqual(text, 'hello')
        self.assertIn('choices', raw)

    def test_simple_prompt_uses_system(self) -> None:
        with patch('src.deepseek_client.chat_completion') as mock_cc:
            mock_cc.return_value = ('ok', {})
            out = simple_prompt('u', system='sys', api_key='k')
        self.assertEqual(out, 'ok')
        args, kwargs = mock_cc.call_args
        self.assertEqual(
            args[0],
            [{'role': 'system', 'content': 'sys'}, {'role': 'user', 'content': 'u'}],
        )
        self.assertEqual(kwargs.get('api_key'), 'k')
