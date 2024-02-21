from wagtail.snippets.views.snippets import SnippetViewSet, SnippetViewSetGroup
from wagtail.snippets.models import register_snippet


from .models import PricingFeature, PricingTier


class TierSnippetView(SnippetViewSet):
    model = PricingTier
    menu_label = 'Pricing Tiers'
    icon = 'price'


class FeatureViewSet(SnippetViewSet):
    model = PricingFeature
    menu_label = 'Pricing Features'
    icon = 'checklist'


class PricingFeaturesViewSetGroup(SnippetViewSetGroup):
    menu_label = 'Pricing Snippet'
    menu_order = 200
    items = (FeatureViewSet,)

register_snippet(PricingFeaturesViewSetGroup)
