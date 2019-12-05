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
from nva.chemiedp.hersteller import IHersteller
from collective.z3cform.datagridfield import DictRow, DataGridFieldFactory
from nva.chemiedp.vocabularies import hskategorieVocabulary

class ILink(form.Schema):

    title = schema.TextLine(title = u"Titel des Links")
    url = schema.URI(title = u"URL des Links")

class IVerdampfung(form.Schema):

    bahn_150 = schema.Float(title = u"150")
    bahn_160 = schema.Float(title = u"160", required=False)
    bahn_170 = schema.Float(title = u"170", required=False)
    bahn_180 = schema.Float(title = u"180", required=False)


class IHeatsetwaschmittel(form.Schema, IImageScaleTraversable):
    """
    Description of the Example Type
    """

    form.widget(verdampfung=DataGridFieldFactory)

    hersteller = RelationChoice(title = _(u"Hersteller"),
            description = _(u"Bitte wählen Sie hier den Hersteller des Reinigungsmittels aus."),
            source=ObjPathSourceBinder(object_provides=IHersteller.__identifier__),
            required = True,)

    verdampfung = schema.List(title = _(u"Verdampungsfaktoren"),
            description = _(u"Bitte tragen Sie hier die Verdampfungsfaktoren fuer die entsprechenden Bahntemperaturen ein"),
            value_type=DictRow(title=u"Verdampfungsfaktoren", schema=IVerdampfung),
            required = False,)

    emissionsgeprueft = schema.Bool(title = _(u"Emissionsarmes Produkt"),
            description = _(u"Bitte markieren Sie hier, wenn für das Produkt die Kriterien des Gütesiegels\
                              erfüllt sind."),
            required = False,)

    ueg = schema.TextLine(title = _(u"UEG in g/m3"), required=False)

    response = schema.TextLine(title = _(u"Responsefaktor"), required=False)

    hskategorie = schema.Choice(title=u"Hautschutzmittelgruppe", 
            vocabulary=hskategorieVocabulary, 
            required=False)

    pruefdateum = schema.Date(title = _(u"Prüfdatum"),
            required = False,)

class Heatsetwaschmittel(Container):
    grok.implements(IHeatsetwaschmittel)

    # Add your class methods and properties here

class SampleView(grok.View):
    """ sample view class """

    grok.context(IHeatsetwaschmittel)
    grok.require('zope2.View')

    # grok.name('view')

    # Add view methods here
