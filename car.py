class Car(object):
  def __init__(self, car_type = None , car_model = None, car_name =None ):
    self.car_type = car_type
    self.car_model = car_model
    self.num_of_doors = 2

    if model is None:
      self.car_model = "GM"
    else:
      self.car_model = car_model

    if name is None:
      self.car_name = "General"
    else:
      self.car_name = car_name

  def num_of_doors(self):
   if self.car_type != "porshe" or "Koenigsegg": #num of doors are expected to be 4 except for porsche and koenigsegg
     self.num_of_doors = 4
     return self
   return self.num_of_doors

  def num_of_wheels(self):
    if self.car_type != "trailer": #number of wheels are expected to be 4 except for trailers which can have 8
      return 4
    else:
      return 8

   def car_model(self):
    if self.car_model == "corolla":
      return True
    