from abc import ABC, abstractmethod
from typing import List, Dict


class DataCSVRepository(ABC):

    @abstractmethod
    def get_data_from_csv(self, file_name: str) -> List[Dict]:
        """Get a Transactions object list from a given csv."""

        pass
