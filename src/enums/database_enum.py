from enum import IntEnum

class DatabaseEnum(IntEnum):
    POSTGRES = 1
    MYSQL = 2

    @classmethod
    def to_sql_list(cls):
        return f"({','.join( ( str(enum.value) for enum in cls ) )})"