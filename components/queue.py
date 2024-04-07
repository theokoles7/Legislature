"""Legislature job queue implementation."""

from components.task    import Task

class Queue():
    """Queue class."""
    
    # Field list
    __jobs: list
    
    # Dunders
    def __init__(self, job_list: list[Task] = list()):
        """Initialize Task Queue object.

        Args:
            job_list (list[Task], optional): List of Tasks. Defaults to empty queue.
        """
        self.__jobs = job_list