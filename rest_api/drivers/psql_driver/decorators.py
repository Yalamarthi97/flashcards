from functools import wraps
import traceback


def use_cursor(function):
    @wraps(function)
    def wrapped_function(*args, **kwargs):
        cur = args[0].conn.cursor()
        response = function(*args, **kwargs, cursor=cur)
        cur.close()
        return response

    return wrapped_function


def do_in_transaction(function):
    @wraps(function)
    def wrapped_function(*args, **kwargs):
        cursor = kwargs.__getitem__("cursor")
        try:
            cursor.execute("""BEGIN;""")
            response = function(*args, **kwargs)
            cursor.execute("""COMMIT;""")
            return response
        except Exception as e:
            traceback.print_exc()
            cursor.execute("""ROLLBACK;""")

    return wrapped_function
