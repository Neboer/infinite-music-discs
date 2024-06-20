# -*- coding: utf-8 -*-
#
#Infinite Music Discs resourcepack contents abstract factory module
#Generation tool, datapack design, and resourcepack design by link2_thepast

from src.contents.resourcepack.v1.factory import Resourcepackv1Factory
from src.contents.resourcepack.v2.factory import Resourcepackv2Factory

factory_v1 = Resourcepackv1Factory()
factory_v2 = Resourcepackv2Factory()

# Abstract factory to select which pack factory should be used to generate
#   the resourcepack based on the version the user wants. Returns an instance of ResourcepackContents
#   generated by the chosen factory
def get(pack_format: int):

    if factory_v2.min_pack_format <= pack_format:
        sel_factory = factory_v2

    else:
        sel_factory = factory_v1

    return sel_factory.get(pack_format)
