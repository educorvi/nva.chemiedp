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
from collective.z3cform.datagridfield import DictRow, DataGridFieldFactory
from nva.chemiedp.hersteller import IHersteller
from nva.chemiedp.maschine import IMaschine
from nva.chemiedp.vocabularies import wmklasse, institute, dmvocab, wmkategorie
from nva.chemiedp.vocabularies import hskategorieVocabulary
from nva.chemiedp import MessageFactory as _


# Interface class; used to define content-type schema.

class IChemikalien(form.Schema):

    gefahrstoff = schema.TextLine(title = u"Gefahrstoff / Chemikalie")
    cas = schema.TextLine(title = u"CAS-Nummer", required=False)
    anteil = schema.TextLine(title = u"Anteil")


class IProduktdatenblatt(form.Schema, IImageScaleTraversable):
    """
    Datenblatt eines Produkts
    """

    hersteller = RelationChoice(title = _(u"Hersteller"),
                 description = _(u"Bitte wählen Sie hier den Hersteller des Wasch- und Reingigungsmittels aus."),
                 source=ObjPathSourceBinder(object_provides=IHersteller.__identifier__),
                 required = True,)

    produktkategorie = schema.List(title = _(u"Produktkategorie"),
            description = _(u"Bitte wählen Sie eine Produktkategorie für das Wasch- und Reinigungsmittel aus."),
            value_type = schema.Choice(source = wmkategorie),
            required = True,)

    produktklasse = schema.Choice(title = _(u"Produktklasse"),
            description = _(u"Bitte wählen Sie eine Produktklasse für das Waschn- und Reinigungsmittel aus."),
            vocabulary = wmklasse,
            required = True,)

    flammpunkt = schema.Int(title = _(u"Flammpunkt"),
            description = _(u"Bitte geben Sie hier den Wert des Flammpunktes in Grad Celsius an."),
            required = False,)

    form.widget(chemikalienliste=DataGridFieldFactory)
    chemikalienliste = schema.List(title = u'EG Sicherheitsdatenblatt',
                        description=u'Zusammensetzung/Angaben zu Bestandteilen',
                        value_type=DictRow(title=u"Chemikalien", schema=IChemikalien),
                        required = False,)

    wertebereich = schema.Bool(title = _(u"Wertebereich für den Flammpunkt"),
            description = _(u"Bitte treffen Sie hier eine Auswahl wenn der Wertebereich für den\
                              Flammpunkt größer als der angegebene Zahlenwert ist."),
            required = False,)

    emissionsgeprueft = schema.Bool(title = _(u"Emissionsarmes Produkt"),
            description = _(u"Bitte markieren Sie hier, wenn für das Produkt die Kriterien des Gütesiegels\
                              erfüllt sind."),
            required = False,)

    maschinen = schema.List(title = _(u"Druckmaschinen und automatische Waschanlagen"),
            description = _(u"Bitte geben Sie hier die Druckmaschinen und automatischen Waschanlagen an,\
                              für das dieses Wasch- und Reinigungsmittel zugelassen wurde."),
            value_type = schema.Choice(source = dmvocab),
            required = True,)

    materialvertraeglichkeit = schema.Choice(title = _(u"Materialverträglichkeit"),
            description = _(u"Bitte wählen Sie hier die Institute aus, von denen die Materialverträglichkeit getestet wurde."),
            vocabulary = institute,
            required = True,)

    hskategorie = schema.Choice(title=u"Hautschutzmittelgruppe", 
            vocabulary=hskategorieVocabulary, 
            required=False)

    bemerkungen = RichText(title=_(u"Bemerkungen"),
                  description=_(u"Hier können zusätliche Bemerkungen zum Produktdatenblatt eingefügt werden."),
                  required=False,)


class Produktdatenblatt(Container):
    grok.implements(IProduktdatenblatt)

    # Add your class methods and properties here


# View class
# The view will automatically use a similarly named template in
# produktdatenblatt_templates.
# Template filenames should be all lower case.
# The view will render when you request a content object with this
# interface with "/@@sampleview" appended.
# You may make this the default view for content objects
# of this type by uncommenting the grok.name line below or by
# changing the view class name and template filename to View / view.pt.

class SampleView(grok.View):
    """ sample view class """

    grok.context(IProduktdatenblatt)
    grok.require('zope2.View')

    # grok.name('view')

    # Add view methods here
