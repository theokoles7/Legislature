"""Legislature Task class and utilities."""

import itertools

class Task():
    """Legislature Task class."""
    # Class Attribute(s)
    job_id: int =   itertools.count()
    
    # Field list
    __id:               int
    __arrival_time:     int
    __burst_time:       int
    __priority:         int
    __start_time:       int = None
    __run_time:         int = None
    __wait_time:        int = None
    __end_time:         int = None
    __completion_time:  int = None
    
    # Dunders =====================================================================================
    def __init__(self, arrival_time: int, burst_time: int, priority: int):
        """Initialize Job object.

        Args:
            id              (int): Job id.
            arrival_time    (int): Job's arrival time.
            burst_time      (int): Job's required burst time.
            priority        (int): Job's priority.
        """
        self.__id =             f"P-{next(Task.job_id)}"
        self.__arrival_time =   arrival_time
        self.__burst_time =     burst_time
        self.__priority =       priority
        
    def __str__(self) -> str:
        """Provide string format of Task object.

        Returns:
            str: String format of Task object.
        """
        return (
            f"Task(id: {self.__id}, arrival_time: {self.__arrival_time}, burst_time: {self.__burst_time}, "
            f"priority: {self.__priority}, start_time: {self.__start_time}, run_time: {self.__run_time}, "
            f"wait_time: {self.__wait_time}, end_time: {self.__end_time}, completion_time: {self.__completion_time})"
        )
    
    def __tuple__(self) -> tuple:
        """Provide array format of Task object.

        Returns:
            tuple: Tuple format of Task object.
        """
        return [
            self.__id,
            self.__arrival_time,
            self.__burst_time,
            self.__priority,
            self.__start_time,
            self.__run_time,
            self.__wait_time,
            self.__end_time,
            self.__completion_time
        ]
        
    def __dict__(self) -> dict:
        """Provide dictionary format of Task object.

        Returns:
            dict: Dictionary format of Task object.
        """
        return {
            "id":               self.__id,
            "arrival_time":     self.__arrival_time,
            "burst_time":       self.__burst_time,
            "priority":         self.__priority,
            "start_time":       self.__start_time,
            "run_time":         self.__run_time,
            "wait_time":        self.__wait_time,
            "end_time":         self.__end_time,
            "completion_time":  self.__completion_time
        }
    
    # Accessors/Mutators ==========================================================================
    def id(self, id: int = None) -> int:
        """Access/mutate Task id attribute.

        Args:
            id (int, optional): New value for Task ID attribute. Defaults to None.

        Returns:
            int: Task ID attribute.
        """
        # If new ID is provided, assign the new ID
        if id: self.__id = id
        
        # Return ID
        return self.__id
    
    def arrival_time(self, arrival_time: int = None) -> int:
        """Access/mutate Task arrival time attribute.

        Args:
            arrival_time (int, optional): New value for Task arrival time attribute.. Defaults to None.

        Returns:
            int: Task arrival time attribute.
        """
        # If new arrival time is provided, assign the new arrival time
        if arrival_time: self.__arrival_time = arrival_time
        
        # Return arrival time
        return self.__arrival_time
    
    def burst_time(self, burst_time: int = None) -> int:
        """Access/mutate Task burst time attribute.

        Args:
            burst_time (int, optional): New value for Task burst time attribute. Defaults to None.

        Returns:
            int: Task burst time attribute.
        """
        # If new burst time is provided, assign the new burst time
        if burst_time: self.__burst_time = burst_time
        
        # Return burst time
        return self.__burst_time
    
    def priority(self, priority: int = None) -> int:
        """Access/mutate Task priority attribute.

        Args:
            priority (int, optional): New value for Task priority attribute. Defaults to None.

        Returns:
            int: New value for Task priority attribute.
        """
        # If new priority is provided, assign the new priority
        if priority: self.__priority = priority
        
        # Return priority
        return self.__priority
        
    def start_time(self, start_time: int = None) -> int:
        """Access/mutate Task start time attribute.

        Args:
            start_time (int, optional): New value for Task start time attribute. Defaults to None.

        Returns:
            int: Task start time attribute.
        """
        # If new start time is provided, assign the new start time
        if start_time: self.__start_time = start_time
        
        # Return start time
        return self.__start_time
    
    def end_time(self, end_time: int = None) -> int:
        """Access/mutate Task end time attribute.

        Args:
            end_time (int, optional): New value for Task end time attribute. Defaults to None.

        Returns:
            int: Task end time attribute.
        """
        # If new end tiem is provided, assign the new end time
        if end_time: self.__end_time = end_time
        
        # Return end time
        return self.__end_time
    
    def completion_time(self, completion_time: int = None) -> int:
        """Access/mutate Task completion time attribute.

        Args:
            completion_time (int, optional): New value for Task completion time attribute. Defaults to None.

        Returns:
            int: Task completion time attribute.
        """
        # If new completion time is provided, assign the new completion time
        if completion_time: self.__completion_time = completion_time
        
        # Return completion time
        return self.__completion_time
    
    # Methods =====================================================================================
    def burst(self, time: int) -> int:
        """Increment Task run time attribute.
        
        Args:
            time (int): Time at which burst is being executed

        Returns:
            int: Task's remaining burst time
        """
        if self.__start_time is None: self.__start_time = time
        
        self.__run_time += 1
        
        if self.__burst_time == 0: 
            self.__end_time =   time
            self.__wait_time =  self.__end_time = self.__start_time - self.__burst_time
        
        return self.__burst_time - self.__run_time