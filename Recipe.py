class Recipe:
    def __init__(self):
        """Initialize the Recipe with empty lists for ingredients and steps."""
        self.ingredients = []
        self.steps = []

    def add_ingredients(self):
        """Prompt the user to enter the details of ingredients and store them."""
        num_ingredients = int(input("Enter the number of ingredients: "))
        for i in range(num_ingredients):
            print(f"Enter details for ingredient {i + 1}:")
            name = input("Name: ")
            quantity = float(input("Quantity: "))
            unit = input("Unit: ")
            self.ingredients.append({'name': name, 'quantity': quantity, 'unit': unit})

    def add_steps(self):
        """Prompt the user to enter the details of steps and store them."""
        num_steps = int(input("Enter the number of steps: "))
        for i in range(num_steps):
            print(f"Enter details for step {i + 1}:")
            description = input("Description: ")
            self.steps.append({'description': description})

    def display_recipe(self):
        """Display the recipe with ingredients and steps."""
        print("\nRecipe:")
        print("Ingredients:")
        for ingredient in self.ingredients:
            print(f"{ingredient['quantity']} {ingredient['unit']} of {ingredient['name']}")
        
        print("Steps:")
        for i, step in enumerate(self.steps, start=1):
            print(f"{i}. {step['description']}")

    def scale_recipe(self, factor):
        """Scale the quantity of each ingredient by the given factor."""
        for ingredient in self.ingredients:
            ingredient['quantity'] *= factor
        print("Recipe scaled successfully.")

    def clear_data(self):
        """Clear all ingredients and steps."""
        self.ingredients = []
        self.steps = []
        print("All data cleared. Enter a new recipe.")

    def run(self):
        """Run the recipe program."""
        print("Enter the details for the recipe:")
        self.add_ingredients()
        self.add_steps()
        self.display_recipe()

        factor = float(input("Enter a scaling factor (0.5, 2, or 3): "))
        self.scale_recipe(factor)
        self.display_recipe()

        reset_choice = input("Do you want to reset quantities to original values? (yes/no) ")
        if reset_choice.lower() == "yes":
            print("Reset quantities functionality is not implemented yet.")

        clear_choice = input("Do you want to clear all data? (yes/no) ")
        if clear_choice.lower() == "yes":
            self.clear_data()


# Run the program
if __name__ == "__main__":
    recipe = Recipe()
    recipe.run()
