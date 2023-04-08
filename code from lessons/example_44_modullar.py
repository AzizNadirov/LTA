variable = 'var'

print("example_44_modullar is runnung...")

def make_discout(price, discout):
    assert price > discout, "Endirimli qiymet malin oz qiymetinden kichik ola bilmez.."
    return price - discout

