"""
Доменные классы управления заводом.

Module: factory.domain.management

Note:
    Пакет намеренно не реэкспортирует классы во избежание
    циклических импортов. Импортируйте конкретные модули:

    .. code-block:: python

        from factory.domain.management.factory import Factory
        from factory.domain.management.department import Department
        from factory.domain.management.report import Report
        from factory.domain.management.statistics import Statistics
"""