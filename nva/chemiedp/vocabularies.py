# -*- coding: utf-8 -*-
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm
from Products.CMFCore.utils import getToolByName
from nva.chemiedp import MessageFactory as _
from five import grok
from zope.schema.interfaces import IContextSourceBinder

hskategorien = [
    SimpleTerm(u"id_wasserloeslich", u"wasserloeslich", u"gegen wasserlösliche Arbeitsstoffe"),
    SimpleTerm(u"id_nichtwasserloeslich", u"nichtwasserloeslich", u"gegen wasserunlösliche Arbeitsstoffe"),
    SimpleTerm(u"id_wechselnd", u"wechselnd", u"gegen wechselnde Arbeitsstoffe")]
hskategorieVocabulary = SimpleVocabulary(hskategorien)

klasse = SimpleVocabulary(
    [SimpleTerm(value=u'fein', title=_(u'fein')),
     SimpleTerm(value=u'mittel', title=_(u'mittel')),
     SimpleTerm(value=u'grob', title=_(u'grob'))]
    )

ausgangsmaterial = SimpleVocabulary(
    [SimpleTerm(value=u'Staerke', title=_(u'Stärke')),
     SimpleTerm(value=u'Calciumcarbonat', title=_(u'Calciumcarbonat')),
     SimpleTerm(value=u'Zucker', title=_(u'Zucker'))]
    )

anwendungsgebieteVocab = SimpleVocabulary(
    [SimpleTerm(value=u'Farbreiniger', title=_(u'Farbreiniger')),
     SimpleTerm(value=u'Plattenreiniger', title=_(u'Plattenreiniger')),
     SimpleTerm(value=u'Feuchtwalzenreiniger', title=_(u'Feuchtwalzenreiniger')),
     SimpleTerm(value=u'Gummituchregenerierer', title=_(u'Gummituchregenerierer')),
     SimpleTerm(value=u'Reiniger_Leitstaende_Sensoren', title=_(u'Reiniger für Leitstände, Sensoren')),
     SimpleTerm(value=u'Klebstoffreiniger', title=_(u'Klebstoffreiniger')),]
    )

einstufungVocab = SimpleVocabulary(
    [SimpleTerm(value=u'xi-reizend', title=_(u'Xi; Reizend')),
     SimpleTerm(value=u'xn-gesundheitsschaedlich', title=_(u'Xn; gesundheitsschädlich')),
     SimpleTerm(value=u'signalwort-achtung', title=_(u'Signalwort: Achtung')),
     SimpleTerm(value=u'signalwort-gefahr', title=_(u'Signalwort: Gefahr')),
     SimpleTerm(value=u'piktogramm-achtung', title=_(u'Piktogramm: Achtung')),
     SimpleTerm(value=u'piktogramm-aetzend', title=_(u'Piktogramm: Ätzend')),
     SimpleTerm(value=u'piktogramm-entflammbar', title=_('Piktogramm: Entflammbar')),]
    )

zweckVocab = SimpleVocabulary(
    [SimpleTerm(value=u'buchdruck', title=_(u'Buchdruck')),
     SimpleTerm(value=u'flexodruck', title=_(u'Flexodruck')),
     SimpleTerm(value=u'siebdruck', title=_(u'Siebdruck')),
     SimpleTerm(value=u'farbreiniger_alle_druckverfahren', title=_(u'Farbreiniger alle Druckverfahren')),
     SimpleTerm(value=u'offsetdruck', title=_(u'Offsetdruck')),
     SimpleTerm(value=u'waschanlage', title=_(u'Waschanlage')),
     SimpleTerm(value=u'tiefdruck', title=_(u'Tiefdruck')),
     SimpleTerm(value=u'klebstoffreiniger', title=_(u'Klebstoffreiniger')),
     SimpleTerm(value=u'uv-offsetdruck', title=_(u'UV-Druck')),
     SimpleTerm(value=u'klischeereiniger', title=_(u'Klischeereiniger')),
     SimpleTerm(value=u'bodenreiniger', title=_(u'Bodenreiniger')),
     SimpleTerm(value=u'entfetter', title=_(u'Entfetter')),
     SimpleTerm(value=u'reflektorreiniger', title=_(u'Reflektorreiniger')),]
     )

institute = SimpleVocabulary(
    [SimpleTerm(value=u'FOGRA', title=_(u'FOGRA')),
     SimpleTerm(value=u'nicht getestet', title=_(u'nicht auf Materialverträglichkeit getestet.')),]
    )

wmkategorie = SimpleVocabulary(
    [SimpleTerm(value=u"UV-Druck", title=_(u'UV-Druck')),
     SimpleTerm(value=u'Konventioneller Druck', title=_(u'Konventioneller Druck')),]
    )

wmklasse = SimpleVocabulary(
    [SimpleTerm(value=u'Reinigungsoele auf Pflanzenoelbasis', title=_(u'Waschmittel auf Pflanzenölbasis')),
     SimpleTerm(value=u'UV-Waschmittel', title=_(u'UV-Waschmittel')),
     SimpleTerm(value=u'Waschmittel auf Kohlenwasserstoffbasis', title=_(u'Waschmittel auf Kohlenwasserstoffbasis')),
     SimpleTerm(value=u'Waschmittel auf Basis Testbenzin', title=_(u'Waschmittel auf Basis Testbenzin')),
     SimpleTerm(value=u'Wasch- und Reinigungsmittel auf waessriger Basis/Emulsionen', 
                title=_(u'Waschmittel auf wässriger Basis/Emulsionen')),]
    )

@grok.provider(IContextSourceBinder)
def dmvocab(context):
    """ Listet die Druckmaschinen mit ihren Herstellern """
    terms = []
    if context:
        pcat = getToolByName(context, 'portal_catalog')
        brains = pcat(Language = 'all', portal_type = 'nva.chemiedp.maschine', 
                      sort_on = "sortable_title", sort_order = "asc", show_inactive = True)
        for i in brains:
            obj = i.getObject()
            titel = u"%s - %s" % (obj.title, obj.hersteller.to_object.title)
            terms.append(SimpleTerm(value = i.id, title = titel))
    return SimpleVocabulary(terms)
