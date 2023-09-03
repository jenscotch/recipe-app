from django.test import TestCase
from .models import Recipe
from .forms import RecipesSearchForm

# Create your tests here.

class RecipeModelTest(TestCase):

    def setUpTestData():
        Recipe.objects.create(name='Tea', cooking_time='5', ingredients='Tea, Water, Sugar')

    def test_recipe_name(self):
        recipe = Recipe.objects.get(id=1)
        field_label = recipe._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')

    def test_recipe_name_max_length(self):
        recipe = Recipe.objects.get(id=1)
        max_length = recipe._meta.get_field('name').max_length
        self.assertEqual(max_length, 120)

    def test_cooking_time_helptext(self):
        recipe = Recipe.objects.get(id=1)
        recipe_cookingtime = recipe._meta.get_field('cooking_time').help_text
        self.assertEqual(recipe_cookingtime, 'in minutes')

class RecipesSearchFormTest(TestCase):

    def test_form_render_recipe_diff_input(self):
        form = RecipesSearchForm()
        self.assertIn('recipe_diff', form.as_p())

    def test_form_renders_chart_type_input(self):
        form = RecipesSearchForm()
        self.assertIn('chart_type', form.as_p())

    def test_form_valid_data(self):
        form = RecipesSearchForm(
            data = {'recipe_diff': '#1', 'chart_type': '#2'}
        )
        self.assertTrue(form.is_valid())

    def test_form_invalid_data(self):
        form = RecipesSearchForm(
            data = {'recipe_diff': '', 'chart_type': ''}
        )
        self.assertFalse(form.is_valid())