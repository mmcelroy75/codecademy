class Art:
  
  def __init__(self, artist, title, medium, year, owner):
    self.artist = artist
    self.title = title
    self.medium = medium
    self.year = year
    self.owner = owner
    
  def __repr__(self):
    return self.artist + ". " + '"%s"' % self.title + ". " + str(self.year) + ", " + self.medium + ". " + self.owner.name + ", " + self.owner.location + "."

 
class Marketplace(list):

  def __init__(self):
    self.listings = []
    
  def __repr__(self):
    return self.listings
  
  #def __iter__(self):
    #return self.listings
    
  def add_listing(self, new_listing):
    self.listings.append(new_listing)
    return self.listings
  
  def remove_listing(self, listing):
    self.listings.remove(listing)
    return self.listings
  
  def show_listings(self):
    print("The following pieces are available for sale:\n")
    for listing in self.listings:
      print(f"{listing.art}, {listing.price}\n")
      

class Client:
  
  def __init__(self, name, location, is_musuem):
    self.name = name
    self.location = location
    self.is_museum = bool
    
  def sell_artwork(self, artwork, price):
    self.artwork = artwork
    self.price = price
    if artwork.owner == self:
      new_listing = Listing(self.artwork, self.price, artwork.owner)
      veneer.add_listing(new_listing)
      
  def buy_artwork(self, artwork):
    if artwork.owner != self:
      for listing in veneer.listings:
        if listing.art == artwork:
          art_listing = artwork
          artwork.owner = self
          veneer.remove_listing(listing)
        #else:
          #print("That piece is not available for sale.")
          
    
class Listing:
  
  def __init__(self, art, price, seller):
    self.art = art
    self.price = price
    self.seller = seller
  
  def __repr__(self):
    return self.art, self.price

edytta = Client("Edytta Halpirt", "Private Collection", False)
jjones = Client("Jim Jones", "Private Collection", False)
lbrown = Client("Leroy Brown", "Private Collection", False)

moma = Client("The MOMA", "New York", True)

girl_with_mandolin = Art("Picasso, Pablo", "Girl with a Mandolin (Fanny Tellier)","oil on canvas", 1910, jjones)
v_with_fog = Art("Monet, Claude", "Vétheuil in the Fog", "oil on canvas", 1879, edytta)
the_sleeper = Art("di Lempicka, Tamara", "The Sleeper", "oil on canvas", 1932, lbrown)

#print(girl_with_mandolin)
      
veneer = Marketplace()

jjones.sell_artwork(girl_with_mandolin, "$6M (USD)")
edytta.sell_artwork(v_with_fog, "$5M (USD)")
lbrown.sell_artwork(the_sleeper, "$4M (USD)")


#veneer.show_listings()
moma.buy_artwork(girl_with_mandolin)
moma.buy_artwork(v_with_fog)
moma.buy_artwork(the_sleeper)
veneer.show_listings()

print(girl_with_mandolin)
print(v_with_fog)
print(the_sleeper)
