# -*- coding: utf-8 -*-

from zope.interface import implements

from imio.urban.dataimport.urbaweb.importer import UrbawebDataImporter
from brainelechateau.urban.dataimport.interfaces import IBrainelechateauDataImporter


class BrainelechateauDataImporter(UrbawebDataImporter):
    """ """

    implements(IBrainelechateauDataImporter)
