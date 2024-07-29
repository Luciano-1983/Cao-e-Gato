def determine_winner(rex, bob, oli):
    # Calcula a distância de cada cachorro até o gato
    distancia_rex = abs(rex - oli)
    distancia_bob = abs(bob - oli)
    
    # Compara as distâncias
    if distancia_rex < distancia_bob:
        return "Rex"
    elif distancia_bob < distancia_rex:
        return "Bob"
    else:
        return "Oli"

# Exemplo de uso
rex_pos = 2
bob_pos = 7
oli_pos = 5
print(determine_winner(rex_pos, bob_pos, oli_pos))  # Output: "Bob"
