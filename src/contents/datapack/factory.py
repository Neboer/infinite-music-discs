# -*- coding: utf-8 -*-
#
#Infinite Music Discs datapack contents abstract factory module
#Generation tool, datapack design, and resourcepack design by link2_thepast

from src.contents.datapack.v2.factory import Datapackv2Factory
from src.contents.datapack.v3.factory import Datapackv3Factory

factory_v2 = Datapackv2Factory()
factory_v3 = Datapackv3Factory()

# Abstract factory to select which datapack factory should be used to generate
#   the datapack based on the version the user wants. Returns an instance of DatapackContents
#   generated by the chosen factory
def get(pack_format: int):

    if factory_v3.min_pack_format <= pack_format:
        sel_factory = factory_v3

    elif factory_v2.min_pack_format <= pack_format:
        sel_factory = factory_v2

    else:
        #TODO: v1 datapack?
        pass

    return sel_factory.get(pack_format)
