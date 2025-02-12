#!/usr/bin/env python3
#
# Copyright (c) 2012-2022 Snowflake Computing Inc. All rights reserved.
#
"""Context module for Snowpark."""
import snowflake.snowpark

_use_sql_simplifier = True
_use_scoped_temp_objects = True
# TODO: consider moving it to __init__.py


def get_active_session() -> "snowflake.snowpark.Session":
    """Returns the current active Snowpark session.

    Raises: SnowparkSessionException: If there is more than one active session or no active sessions.

    Returns:
        A :class:`Session` object for the current session.
    """
    return snowflake.snowpark.session._get_active_session()
