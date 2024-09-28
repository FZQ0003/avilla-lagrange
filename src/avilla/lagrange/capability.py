from avilla.core.event import AvillaEvent
from avilla.core.ryanvk.collector.application import ApplicationCollector
from avilla.standard.core.application import AvillaLifecycleEvent
from graia.amnesia.message import Element, MessageChain
from graia.ryanvk import Fn, TypeOverload

from .types import Element as LgrElement
from .types import Event as LgrEvent


class LagrangeCapability(ApplicationCollector()._):  # noqa
    @Fn.complex({TypeOverload(): ['raw_event']})
    async def event_callback(self, raw_event: LgrEvent) -> AvillaEvent | AvillaLifecycleEvent | None:
        ...

    @Fn.complex({TypeOverload(): ['raw_element']})
    async def deserialize_element(self, raw_element: LgrElement) -> Element | None:
        ...

    @Fn.complex({TypeOverload(): ['element']})
    async def serialize_element(self, element: Element) -> LgrElement | None:
        ...

    async def deserialize_chain(self, chain: list[LgrElement]) -> MessageChain:
        return MessageChain([__ for _ in chain if (__ := await self.deserialize_element(_))])

    async def serialize_chain(self, chain: MessageChain) -> list[LgrElement]:
        return [__ for _ in chain if (__ := await self.serialize_element(_))]

    async def handle_event(self, event: LgrEvent):
        maybe_event = await self.event_callback(event)

        if maybe_event is not None:
            # if (cx := getattr(maybe_event, 'context', None)) and cx.client.last_value == cx.self.last_value:
            #     return  # Do not record again
            self.avilla.event_record(maybe_event)
            self.avilla.broadcast.postEvent(maybe_event)  # TODO: dispatcher to directly handle client & event
