"""Base classes for services"""

from abc import ABC
from abc import abstractmethod
from typing import Any


class BaseService(ABC):
    """Base class for injectable services"""

    @abstractmethod
    def start(self, *args, **kwargs) -> Any:
        """Start the service"""
