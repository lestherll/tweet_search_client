from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class URL(str):
    """A minimal str subclass for easily building URLs
    """

    base: str

    def __str__(self) -> str:
        return self.base

    def __truediv__(self, other: "URL" | str) -> "URL":
        """
        Use division operator to create new URL with `other`

        >>> URL("https://somesite.com")
        'https://somesite.com'
        >>> URL("https://somesite.com") / resource
        'https://somesite.com/resource'

        Args:
            other (URL&quot; | str): resource to add to the base URL

        Returns:
            URL: new URL object with the `other` resource
        """
        return URL("/".join([self.base, other]))
