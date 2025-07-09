import random

respuestas = ["Sí", "No", "Tal vez", "Pregunta de nuevo", "Definitivamente", "Nunca"]

print("🔮 Ouija Digital 🔮")
print("Escribe tu pregunta (solo sí/no):")

while True:
    input("> ")  # Espera pregunta
    print(f"La Ouija dice: {random.choice(respuestas)}\n")