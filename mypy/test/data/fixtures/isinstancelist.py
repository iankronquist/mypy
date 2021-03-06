from typing import builtinclass, Iterable, Iterator, Generic, typevar, List

@builtinclass
class object:
    def __init__(self) -> None: pass

@builtinclass
class type:
    def __init__(self, x) -> None: pass

def isinstance(x: object, t: type) -> bool: pass

@builtinclass
class int:
    def __add__(self, x: int) -> int: pass
@builtinclass
class bool(int): pass
@builtinclass
class str:
    def __add__(self, x: str) -> str: pass
    def __getitem__(self, x: int) -> str: pass

T = typevar('T')

class list(Iterable[T], Generic[T]):
    def __iter__(self) -> Iterator[T]: pass
    def __mul__(self, x: int) -> list[T]: pass
    def __setitem__(self, x: int, v: T) -> None: pass
    def __getitem__(self, x: int) -> T: pass
    def __add__(self, x: List[T]) -> T: pass

