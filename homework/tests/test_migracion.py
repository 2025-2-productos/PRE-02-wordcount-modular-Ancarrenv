import os


def test_migracion():

    if not os.path.exists("data/output/results.tsv"):  ## si el archivo existe
        raise FileNotFoundErrorer("El archivo results.tsv no existe en data/output/")

    results = {}
    ### r de lear y utf-8 quede lindo
    with open("data/output/results.tsv", "r", encoding="utf-8") as f:
        lines = f.readlines()
        for line in lines:
            key, value = line.strip().split(
                "\t"
            )  ## borreme los espacios y particionarlo por tabulador, queda separado
            results[key] = value  ## convierte el valor a entero

    assert results.get("computational", 0) == "3"
    ## que hace assert es una afirmacion, un resultado esperado de falla o no
    ## se puede usar una forma mas efectiva de hacer esto, en vez de  assert cual
    ## el get es un metodo de diccionario que obtiene el valor asociado a la clave especificada
    ##Si la clave existe, devuelve su valor. Si no existe, devuelve None o el valor por defecto que le des
    assert results.get("analytics", 0) == "5"
