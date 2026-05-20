from abc import ABC, abstractmethod

class Observer(ABC):
    @abstractmethod
    def update(self, emitted_id: str) -> None:
        pass


class IDEmitter:
    def __init__(self) -> None:
        self._observers: list[Observer] = []
        self._current_id = ""

    def attach(self, observer: Observer) -> None:
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        if observer in self._observers:
            self._observers.remove(observer)

    def emit_id(self, new_id: str) -> None:
        print(f"\n emitting ID: {new_id} ")
        self._current_id = new_id
        self._notify()

    def _notify(self) -> None:
        for observer in self._observers:
            observer.update(self._current_id)


class IDSubscriber(Observer):
    def __init__(self, class_name: str, own_id: str) -> None:
        self.class_name = class_name
        self.own_id = own_id
    def update(self, emitted_id: str) -> None:
        if emitted_id == self.own_id:
            print(f"[{self.class_name}] match detected,my ID is {self.own_id}")


def main() -> None:
    emitter = IDEmitter()

    sub_a = IDSubscriber("class_A", "a1b2")
    sub_b = IDSubscriber("class_B", "c3d4")
    sub_c = IDSubscriber("class_C", "e5f6")
    sub_d = IDSubscriber("class_D", "g7h8")

    emitter.attach(sub_a)
    emitter.attach(sub_b)
    emitter.attach(sub_c)
    emitter.attach(sub_d)
    ids_to_emit = ["9999", "a1b2", "xxxx", "c3d4", "e5f6", "zzzz", "g7h8", "0000"]

    print('starting ID transmission')
    for identifier in ids_to_emit:
        emitter.emit_id(identifier)


if __name__ == "__main__":
    main()