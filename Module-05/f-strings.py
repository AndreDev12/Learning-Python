mass_percentage = "1/6"
print(f"On the Moon, you would weigh about {mass_percentage} of your weight on Earth.")

print(round(100/6, 1)) # 16.7
# Con f-strings
print(f"On the Moon, you would weigh about {round(100/6, 1)}% of your weight on Earth.")

# Para usar una expresión
subject = "interesting facts about the moon"
heading = f"{subject.title()}"
print(heading)