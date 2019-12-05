# -*- coding: utf-8 -*-
from five import grok

from z3c.form import group, field
from zope import schema
from zope.interface import invariant, Invalid
from zope.schema.interfaces import IContextSourceBinder
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm

from plone.dexterity.content import Container
from plone.directives import dexterity, form
from plone.app.textfield import RichText
from plone.namedfile.field import NamedImage, NamedFile
from plone.namedfile.field import NamedBlobImage, NamedBlobFile
from plone.namedfile.interfaces import IImageScaleTraversable

from z3c.relationfield.schema import RelationList, RelationChoice
from plone.formwidget.contenttree import ObjPathSourceBinder

from nva.chemiedp import MessageFactory as _
from nva.chemiedp.vocabularies import klasse, ausgangsmaterial
from nva.chemiedp.hersteller import IHersteller

# Interface class; used to define content-type schema.

class IDruckbestaeubungspuder(form.Schema, IImageScaleTraversable):
    """
    Description of the Example Type
    """

    hersteller = RelationChoice(title = _(u"Hersteller"),
            description = _(u"Bitte wählen Sie hier den Hersteller des Druckbestäubungspuders aus."),
            source=ObjPathSourceBinder(object_provides=IHersteller.__identifier__),
            required = True,)

    produktklasse = schema.Choice(title = _(u"Produktklasse"),
            description = _(u"Bitte wählen Sie eine Produktklasse für das Druckbestäubungspuder aus."),
            vocabulary = klasse,
            required = True,)

    ausgangsmaterial = schema.Choice(title = _(u"Ausgangsmaterial"),
            description = _(u"Bitte wählen Sie das Ausgangsmaterial für das Druckbestäubungspuder aus."),
            vocabulary = ausgangsmaterial,
            required = True,)

    medianwert = schema.Float(title = _(u"Medianwert in µm"),
            description = _(u"Bitte geben Sie hier den Medianwert in Micrometer als Gleitkommawert an."),
            required = True,)

    volumenanteil = schema.Float(title = _(u"Volumenanteil < 10 µm"),
            description = _(u"Prozentuale Angabe des Volumenanteils der Partikel mit Korngrößen unterhalb\
                              10 µm am Gesamtvolumen der Puderprobe"),
            required = True,)

    maschinen = schema.List(title = _(u"Maschinen mit Ausschlußkriterien"),
            description = _(u"Bitte geben Sie hier Maschinen an, bei denen dieses Druckbestäubungspuder\
                              explizit nicht verwendet werden darf (ein Eintrag pro Zeile)"),
            value_type = schema.TextLine(title = _(u"Druckbestäubungspuder")),
            required = False,)

    emissionsgeprueft = schema.Bool(title = _(u"Emissionsarmes Produkt"),
            description = _(u"Bitte markieren Sie hier, wenn für das Produkt die Kriterien des Gütesiegels\
                              erfüllt sind."),
            default = True,
            required = False,)

    pruefdateum = schema.Date(title = _(u"Prüfdatum"),
            required = False,)


class Druckbestaeubungspuder(Container):
    grok.implements(IDruckbestaeubungspuder)

    # Add your class methods and properties here


# View class
# The view will automatically use a similarly named template in
# druckbestaeubungspuder_templates.
# Template filenames should be all lower case.
# The view will render when you request a content object with this
# interface with "/@@sampleview" appended.
# You may make this the default view for content objects
# of this type by uncommenting the grok.name line below or by
# changing the view class name and template filename to View / view.pt.

class SampleView(grok.View):
    """ sample view class """

    grok.context(IDruckbestaeubungspuder)
    grok.require('zope2.View')

    # grok.name('view')

    # Add view methods here
