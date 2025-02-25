def create_organizational_unit_ldif(filename, ou_name, base_dn):
    """Creates an LDIF file for an organizational unit."""

    ldif_content = f"""# organisational unit for {ou_name} department
dn: ou={ou_name},{base_dn}
changetype: add
objectClass: organizationalUnit
ou: {ou_name}
"""

    try:
        with open(filename, "w") as f:
            f.write(ldif_content)
        print(f"LDIF file '{filename}' created successfully.")
    except Exception as e:
        print(f"Error creating LDIF file '{filename}': {e}")


# Example usage:
filename = "ou.ldif"  # Name of the LDIF file
ou_name = "directores"                   # Name of the organizational unit
base_dn = "dc=example,dc=org"   # Your base DN (replace with your actual DN)

create_organizational_unit_ldif(filename, ou_name, base_dn)


def generar_ou_ldif(grupos, apellido):
    with open(f'oueso1{apellido}.ldif', 'w') as f:
        for grupo in grupos:
            f.write(f"dn: ou={grupo},dc={apellido},dc=org\n")
            f.write("objectClass: organizationalUnit\n")
            f.write(f"ou: {grupo}\n\n")

grupos = ["1ESOA", "1ESOB", "1ESOC", "1ESOD"]
generar_ou_ldif(grupos, "samblas")
