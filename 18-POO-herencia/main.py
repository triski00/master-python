import clases

persona = clases.Persona()
persona.setNombre("Mario")
persona.setApellidos("Avila")
persona.setAltura("182cm")
persona.setEdad("40")

print(f"La persona es: {persona.getNombre()} {persona.getApellidos()}")
print(persona.hablar())
print("----------------------------------")

informatico = clases.Informatico()
informatico.setNombre("Carlos")
informatico.setApellidos("Martinez")

print(f"El informatico es: {informatico.getNombre()} {informatico.getApellidos()}")
print(informatico.getLenguajes())
print(informatico.caminar())

print(informatico.experiencia)



print("----------------------------------")

tecnico = clases.TecnicoRedes()
tecnico.setNombre("Manolo")
print(tecnico.auditarRedes, tecnico.getNombre())





                    


