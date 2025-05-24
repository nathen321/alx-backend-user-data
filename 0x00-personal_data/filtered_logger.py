#!/usr/bin/env python3
"""
Returns the log message obfuscated.
"""

import re
from typing import List


def filter_datum(
    fields: List[str],
    redaction: str,
    message: str,
    separator: str
) -> str:
    """
    Obfuscate specified fields in a log message.

    Args:
        fields: List of field names to redact.
        redaction: String to replace field values with.
        message: The log line containing the fields.
        separator: Character separating fields in the message.

    Returns:
        The log message with specified fields redacted.
    """
    for field in fields:
        pattern = r'({field}=)[^{sep}]+'.format(field=field, sep=separator)
        replacement = f"{field}={redaction}"
        message = re.sub(pattern, replacement, message)
    return message
