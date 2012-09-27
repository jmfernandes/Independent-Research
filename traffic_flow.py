# Defines the Car object and the Lane object. This was built assuming the movement of the cars would be handled by a 'rules' script.

## this part is the rules and the traffic objects

import random

car_type = [1,2,3]

Iden = []

numbers = list(xrange(1,1001))

memory =[]

tel = {'jack': 4098, 'sape': 4139}

#######################################################################################

class GetOutOfLoop( Exception ):
     pass
     ineedthis = 5

#########
class numbersiwant:
	def __init__(self,a):
		self.goodnumber = a
		print a, "a"

numbersiwant(6)

#print thesethings.goodnumber, "this is it"
#########

class Car(object):
    """Defines a Car object with attributes position, speed, and g, where g is
reserved to store the number of empty spaces ahead of the car.
    """
    def __init__(self, position=0, speed=0, identity=0,factor=0,type=0):
        self.position = position
        self.speed = abs(int(random.gauss(int(app.maxvel),2)))
    	"""identity increases in value sequentially for each car (1,2,3,4), factor is a value from 1-100. No two cars have the same factor. Type is the car type 1,2, or 3"""
   	self.g = 0
    	Iden.append(0)
	self.identity= len(Iden)
    	"""above code sets the identity"""
	ranting = random.randint(0,len(numbers))
	self.interation = [0]
	while ranting in memory:
		ranting = random.randint(0,len(numbers))
		self.interation[0] = self.interation[0] +1
		if self.interation[0] == 1200:
			print "too many cars! only 1001 cars allowed"
			#raise GetOutOfLoop
			return
			self.breakingnum = 1
		else:
			self.breakingnum = 2
		"""makes it so that if too many cars are entered, the code doesn't look for an unused number forever"""
	else:
		pass
	memory.append(ranting)
	#print memory, "memory 2"
        self.factor = numbers[memory[self.identity-1]-1]/10.0
	#print self.factor, "self"
   	"""above code sets the factor"""
	typing = random.randint(1, 100)
	if typing <= 10:
		self.type = 1
	elif typing >= 90:
		self.type = 2
	else:
		self.type = 3
    	"""above code sets the type"""

    def __str__(self):
        return 'Position: %d, Speed: %d\nEmpty spaces ahead: %d, Identity: %d, Factor: %g, Type: %d' % (self.position, self.speed, self.g, self.identity,self.factor,self.type)
    def reset(self, position, speed):
        """A slightly more convenient way to set the position and speed simultaneously.
        """
        self.position = position
        self.speed = speed

class Lane(object):
    """Defines a Lane object with attributes length, map, and carlist.
    """
    def __init__(self, spaces=1):
        self.length = spaces
        self.map = []   # uses '_' to represent an empty space, 'n' to represent a space with a car in it.
        self.carlist = []
        for i in range(self.length):
            self.map.append('_')
    def __str__(self):
        return ' '.join(self.map)
    def add_car(self, car):
        """Adds the specified instance 'car' to the lane."""
        if car not in self.carlist:
            self.carlist.append(car)
        self.map_update()
    def remove_car(self, car):
        """Removes the specified instance 'car' from the lane."""
        if car in self.carlist:
            self.carlist.remove(car)
        self.map_update()
    def populate(self, n):
        """Adds n cars to the lane in random positions.
        """
        self.map_update()
        if n > self.map.count('_'):
            if self.map.count('_') == 1: ss = ''
            else: ss = 's'
            if n == 1: ns = ''
            else: ns = 's'
            raise ValueError('Tried to put %d car%s in a lane that has %d empty space%s.' % (n, ns, self.map.count('_'), ss))
        for i in range(n):
            x = random.randint(0, self.length - 1)
            while True:
                if self.map[x] == '_':
                    self.add_car(Car(x))
                    break
                else:
                    x = random.randint(0, self.length - 1)
            self.map_update()
    def map_update(self):
        """Updates the map list to reflect changes in car positions."""
        for spot in range(self.length):
            self.map[spot] = '_'
        for car in self.carlist:
            self.map[car.position] = 'n'
    def g_update_car(self, car):
        """Finds and sets the appropriate g value for a specific car instance.
        """
        self.map_update()
        if car.position != self.length - 1:
            n = car.position + 1
        else:
            n = 0
        count = 0
        while self.map[n] == '_':
            count += 1
            n += 1
            if n > self.length - 1:
                n = n - self.length
        car.g = count
    def g_update_all(self):
        """Finds and sets the appropriate g value for each car instance in the lane.
        """
        for car in self.carlist:
            self.g_update_car(car)
    def print_cars(self):
        """Displays information about each car in 'carlist'. May be useful for debugging, etc.
        """
        for car in self.carlist:
            print '\n', car, '\n' + '-'*27
    def car_positions(self):
        """Returns a list containing the position of each car in carlist."""
        l = []
        for car in self.carlist:
            l.append(car.position)
        return l
    def car_speeds(self):
        """Returns a list containing the speed of each car in carlist."""
        l = []
        for car in self.carlist:
            l.append(car.speed)
        return l
    def move_car(self, car):
        """Changes the position of a given car based on its speed attribute, making sure to loop to the beginning of the lane appropriately."""
        car.position += car.speed
        if car.position > self.length - 1:
            car.position -= self.length
            

class Data(object):
    """A data-holding object which contains histories of each car's position and speed as well as the length of the lane and the number of cars on the lane."""
    def __init__(self):
        self.position_history = []
        self.speed_history = []
        self.lane_length = 0
        self.number_of_cars = 0
    def build_position_history(self, lane):
        for car in lane.carlist:
            self.position_history.append([])
    def append_position_history(self, lane):
        for i in range(len(lane.carlist)):
            self.position_history[i].append(lane.carlist[i].position)
    def build_speed_history(self, lane):
        for car in lane.carlist:
            self.speed_history.append([])
    def append_speed_history(self, lane):
        for i in range(len(lane.carlist)):
            self.speed_history[i].append(lane.carlist[i].speed)
    def update_length(self, lane):
        self.lane_length = lane.length
    def update_number(self, lane):
        self.number_of_cars = len(lane.carlist)



#######################################################################################





def update_and_move(car, lane, vmax, p, cc):
    """To be used only within other rules definitions. Sets the car's speed appropriately, then moves it."""
    #print car.factor, "factor!!!!!"
    #if car.speed > car.g: #stops cars from going through each other.
    #    car.speed = car.g
    if car.speed > car.g*2:
        #print 'yoyoyoyo'
	car.speed = int(round(car.g/2))
    if car.speed > vmax:
	slow_factor = random.randint(1, 100)
	#print slow_factor, "slow factor"
	if car.type == 3:
		if slow_factor <=50:
			car.speed -=1  
			"""regular cars slow down half of the time"""
		else:
			pass
	elif car.type == 2:
		if slow_factor <= 5:
			car.speed -= 1 
			"""fast cars don't slow down often"""
		elif slow_factor >= 90:
			car.speed +=1 
			"""fast cars have a chance of speeding up"""
		else:
			pass
	else:
		car.speed -=1 
		"""slow cars always slow down"""
    if car.speed < car.g and car.speed < vmax:
        car.speed += 1
    if car.speed == vmax:
	super_slow = random.randint(1, 100)
	#print super_slow, "super slow"
	if car.type == 3:
		pass 
		"""regular cars stay the speed limit"""
	elif car.type == 2:
		if super_slow >= 40:
			car.speed +=1 
			"""fast cars speed up"""
		else:
			pass
	else:
		if super_slow <= 20:
			car.speed -=1 
			"""slow cars have a chance of slowing down"""
		else:
			pass	
	#if super_slow <= car.factor:   #adds a probability of randomly slowing down.
	#	car.speed -=1
	#	print super_slow, "its lower!"
	#else:
	#	pass
    #if car.speed == vmax and cc:
    #    prob = 0
    #else:
    #    prob = p
    #if car.speed > 0 and random.randint(1, 100) <= 100*prob:
    #    car.speed -= 1
    if car.speed > car.g: 
        car.speed = car.g
	"""stops cars from going through each other."""
    lane.move_car(car)

def stca(data, lane, vmax, n=10, p=0.50, cc=False):
    """Use the STCA model to simulate the specified lane for 'n' discrete steps with probability 'p' for a car slowing down and with a speed limit of 'vmax' (measured in discrete steps). Setting argument 'cc' to 'True' activates Cruise Control mode. 'data' refers to the data-holding object that will store the simulation's data."""
    data.build_position_history(lane)
    data.build_speed_history(lane)
    data.update_length(lane)
    data.update_number(lane)
    for i in range(n):
        lane.g_update_all()
        for car in lane.carlist:
            update_and_move(car, lane, vmax, p, cc)
        #this is where you want to grab data for graphs, animation, etc.
        #print lane
        data.append_position_history(lane)
        data.append_speed_history(lane)
    lane.g_update_all()
    
def ca184(data, lane, vmax, n=10, cc=False):
    """Use the CA184 model to simulate the specified lane for 'n' discrete steps with a speed limit of 'vmax' (measured in discrete steps). Setting argument 'cc' to 'True' activates Cruise Control mode. 'data' refers to the data-holding object that will store the simulation's data."""
    stca(data,lane, vmax, n, 0, cc)
    
def asep(data, lane, vmax, n=20, p=0, cc=False):
    """Use the ASEP model to simulate the specified lane for 'n' discrete steps with probability 'p' for a car slowing down and with a speed limit of 'vmax' (measured in discrete steps). Setting argument 'cc' to 'True' activates Cruise Control mode. 'data' refers to the data-holding object that will store the simulation's data."""
    data.build_position_history(lane)
    data.build_speed_history(lane)
    data.update_length(lane)
    data.update_number(lane)
    for i in range(n):
        car = random.choice(lane.carlist)
        update_and_move(car, lane, vmax, p, cc)
        #this is where you want to grab data for graphs, animation, etc.
        #print lane
        data.append_position_history(lane)
        data.append_speed_history(lane)
        lane.g_update_all()
    



#######################################################################################




## this part is the visualization

## Defines the Car object and the Lane object. This was built assuming the movement of the cars would be handled by a 'rules' script.

from Tkinter import *
root = Tk()
root.title("Traffic Simulation")
import time

color = ['snow','gainsboro','linen','moccasin','cornsilk','ivory','cornsilk','seashell','honeydew','azure','green','red','blue','turquoise','cyan','aquamarine','chartreuse','yellow','khaki','gold','goldenrod','sienna','peru','burlywood','beige','tan','chocolate','firebrick','orange','coral','tomato','salmon','pink','maroon','magenta','violet','plum','orchid','purple','thistle','slateblue1','royalblue1','lavenderblush1','skyblue1','SpringGreen2','DarkOliveGreen4','IndianRed1']

"""color is a list of words that are recognized by the tkinter package as colors. can be expanded to include a wider variety of colors."""

col =[]
numcar=[]
cars = []
size = []
mode = ['','stca','asep','ca184']
xy = []





#######################################################################################


class ToolTip(object):

    def __init__(self, widget):
        self.widget = widget
        self.tipwindow = None
        self.id = None
        self.x = self.y = 0

    def showtip(self, text):
        "Display text in tooltip window"
        self.text = text
        if self.tipwindow or not self.text:
            return
        x, y, cx, cy = self.widget.bbox("insert")
        x = x + self.widget.winfo_rootx() + 27
        y = y + cy + self.widget.winfo_rooty() +27
        self.tipwindow = tw = Toplevel(self.widget)
        tw.wm_overrideredirect(1)
        tw.wm_geometry("+%d+%d" % (x, y))
        try:
            # For Mac OS
            tw.tk.call("::tk::unsupported::MacWindowStyle",
                       "style", tw._w,
                       "help", "noActivates")
        except TclError:
            pass
        label = Label(tw, text=self.text, justify=LEFT,
                      background="#ffffe0", relief=SOLID, borderwidth=1,
                      font=("tahoma", "8", "normal"))
        label.pack(ipadx=1)

    def hidetip(self):
        tw = self.tipwindow
        self.tipwindow = None
        if tw:
            tw.destroy()

def createToolTip(widget, text):
    toolTip = ToolTip(widget)
    def enter(event):
        toolTip.showtip(text)
    def leave(event):
        toolTip.hidetip()
    widget.bind('<Enter>', enter)
    widget.bind('<Leave>', leave)




#######################################################################################





class App:

    def __init__(self, root):
	self.ii = "foo"
	self.length = 30
	self.lane= Lane(self.length)
	self.data = Data()
	self.data.build_position_history(self.lane)
	self.canvas = Canvas(root,bg="grey", height=100, width=self.length*10,)
	self.DefClr = root.cget("bg")
	self.canvas.pack()

	self.canvas.delete(ALL)
	self.canvas.configure(background=self.DefClr)
	self.lane = Lane(0)

	#root.geometry("650x300")
	self.topframe = Frame(root)
	self.topframe.pack(side=TOP,expand=YES)
	otherframe = Frame(root)
	otherframe.pack(side=LEFT,expand=YES,padx = 5)
	centerframe = Frame(root)
	centerframe.pack(side=LEFT,expand=YES)
	frame = Frame(root)
	frame.pack(side=LEFT,expand=YES,padx = 5)

	self.label = Label(otherframe)
	self.label.pack()

	self.label2 = Label(frame)
	self.label2.pack(side=LEFT)

	self.var = IntVar()
	self.var3 = IntVar()
	self.checkvar = StringVar()
	self.check = Checkbutton(otherframe, text="Cruise Control", variable=self.checkvar, onvalue="True", offvalue="False")
	self.check.pack(side=RIGHT)

	self.var2 = IntVar()
	self.R1 = Radiobutton(otherframe, text="stca", variable=self.var2, value=1, command=self.sel)
	self.R1.pack( anchor = W )

	self.R2 = Radiobutton(otherframe, text="asep", variable=self.var2, value=2, command=self.sel)
	self.R2.pack( anchor = W )
	
	self.R3 = Radiobutton(otherframe, text="ca184", variable=self.var2, value=3, command=self.sel)
	self.R3.pack( anchor = W)
	
	self.R1.select()
	self.check.deselect()
	selection = "traffic simulation in " + str(mode[self.var2.get()]) + " mode"
	self.label.config(text = selection, bg = "grey",bd = 1, relief = SUNKEN)

	#Label(frame, text="probability that drivers will slow down").pack(side=TOP)
	sim = "probability that drivers will slow down:"
	self.label2.config(text = sim)
	self.spin = Spinbox(frame, from_=0, to=1,increment = .1, width = 3)
	self.spin.pack(side=TOP)
	

	Label(centerframe, text="enter the number of cars:").pack(side=TOP)
	
	self.txt_ent = Entry(centerframe)
	self.txt_ent.pack()

	Label(centerframe, text="enter the length of road").pack(side=TOP)
	self.size_ent = Entry(centerframe)
	self.size_ent.pack()

	Label(centerframe, text="enter the duration").pack(side=TOP)
	self.time_ent = Entry(centerframe)
	self.time_ent.pack()

	Label(centerframe, text="enter the max velocity").pack(side=TOP)
	self.velocity_ent = Entry(centerframe)
	self.velocity_ent.pack()

	## enter initial values
	self.txt_ent.insert(0, "10")
	self.size_ent.insert(0, "30")
	self.time_ent.insert(0, "10")
	self.velocity_ent.insert(0, "6")
	##

	## create hover text
	createToolTip(self.check, "determines if cars stay at max speed")
	createToolTip(self.R1, "moves all cars at once")
	createToolTip(self.R2, "moves one car at a time")
	createToolTip(self.R3, "stca model with zero percent probability of slowdown")
	##

	self.quit = Button(centerframe, text="QUIT", fg="red", command=frame.quit)
        self.quit.pack(side=LEFT)

	self.play = Button(centerframe, text="Play", command=self.moving)
        self.play.pack(side=LEFT)

	self.restart = Button(centerframe, text="Create Road", command=self.adding)
        self.restart.pack(side=LEFT)

	#self.create_size = Button(frame, text="Length", command=self.lanesize)
        #self.create_size.pack(side=LEFT)


	self.maxvel = self.velocity_ent.get()

    #def cb(self):
    #    print "variable is", self.var.get()

    def sel(self):
   	selection = "traffic simulation in " + str(mode[self.var2.get()]) + " mode"
	self.label.config(text = selection)




#######################################################################################




    def adding(self):
	#thecars = Car()
	#print thecars.breakingnum, "carssss"
	#print GetOutOfLoop.ineedthis, "whawha"
	#print thesethings.goodnumber, "this is it"
	#print numbersiwant.goodnumber, "what is all this"
	while Iden: 
		Iden.pop(0)
		"""gets rid of the tkinter identity of each car"""
	while memory:
		memory.pop(0)
	if not self.txt_ent.get():
		print 'input the number of cars'
		return
	if not self.size_ent.get():
		print 'input the length of the road'
		return
	if not self.time_ent.get():
		print 'input the duration'
		return
	if not self.velocity_ent.get():
		print 'input a max velocity'
		return
	h=int(self.txt_ent.get())
	gg = int(self.size_ent.get())
	kk = int(self.time_ent.get())
	numcar.append(h)
	pos = self.data.position_history
	vel = self.data.speed_history
	if not pos:
		pass
	else:
		numcar.pop(0)
		while self.pos:
			self.pos.pop(0)
			col.pop(0) 
			vel.pop(0)
			a = self.lane.carlist[0]
			self.lane.remove_car(a)
			for i in range(len(cars)):
				self.canvas.delete(cars[i])
			self.lane.map_update
		while cars:
			cars.pop(0)
	for g in range(h): # creates strings
		x = str(g)
		s = 'mycar' + x
		cars.append(s)
    	"""removes any values from previous simulation is create road is clicked again."""
	self.canvas.destroy()
	## add lane
	self.length = gg
	self.lane= Lane(self.length)
	self.canvas = Canvas(self.topframe,bg="grey", height=100, width=self.length*10)
	#gw = .29 
	#self.canvas.place(relx=gw,rely=0)
	self.canvas.update()
	self.canvas.pack()
	for i in range(1,self.length+1):
		self.canvas.create_line(i*10,0,i*10,100,dash=(3,6))
	##
	self.lane.populate(h)
	duration = kk
	max_v = int(self.velocity_ent.get())
	prob = self.spin.get()
	prob_int = float(prob)
	#print prob
	cruise = self.checkvar.get()
	rad = self.var2.get()
	if rad == 1:
		stca(self.data,self.lane,max_v,duration,prob_int,cruise) ## run code to generate car history
	elif rad == 2:
		asep(self.data,self.lane,max_v,duration,prob_int,cruise)
	else:
		ca184(self.data,self.lane,max_v,duration,cruise)
	self.pos = self.data.position_history
	self.pos.sort()
	for i in range(len(self.pos)):
		self.pos[i] = [x * 10 for x in self.pos[i]]
	for i in range(len(self.pos)):   #need to extract the first value of every list
		rant = random.randint(0,len(color)-1)
		col.append(rant)
		self.canvas.create_rectangle(self.pos[i][0],50,self.pos[i][0]+10,60,fill=color[rant],tags=cars[i])
	#check to make sure cars are obeying print self.data.position_history
	#for i in range(len(self.pos)): #this prints the last position - beware
	#	print self.lane.carlist[i].position
	#print self.pos, "position history"
	#print self.lane.map # map also displays the last position of the cars. data.position_history is the only useful one
	#print self.data.speed_history, "speed history"
	######print self.lane.print_cars()
        



    def moving(self): 
        """the visualization of the blocks moving"""
	if not numcar:
		print 'Create Road First'
		return
	for i in range(len(self.pos)): #resets the rectangles to initial position
		self.canvas.delete(cars[i])
		self.canvas.create_rectangle(self.pos[i][0],50,self.pos[i][0]+10,60,fill=color[col[i]],tags=cars[i])
	self.canvas.update() #this line very necessary to update original positions
	#ind = []
	for i in range(len(self.pos[0])-1):
		time.sleep(0.02)
		xx = 0
		self.canvas.update()
		#x1=0
		while xx < 10:
			xx = xx + 1
			time.sleep(0.05)
			for j in range(len(self.pos)):
				if self.pos[j][i+1] > self.pos[j][i]:
					vel = (self.pos[j][i+1] - self.pos[j][i])/10
					self.canvas.move(cars[j],vel,0)
					self.canvas.update()
				elif self.pos[j][i+1] < self.pos[j][i]:
					#vel2 = (self.length*10 - self.pos[j][i])/10
					#self.canvas.move(cars[j],vel2,0)
					self.canvas.update()
					#if not ind:
					#	pass
					#else:
					#	ind.pop(0)
					#ind.append(j)
					if xx <= 4:
						time.sleep(0.01)
						veloc3 = (self.length*10 - self.pos[j][i])/4.0
						self.canvas.move(cars[j],veloc3,0)
						self.canvas.update()
					elif xx ==5:
						#yy = 0
						#while yy < 10:
						#	yy = yy + 1
						#	#time.sleep(0.015)
						#	vel3 = (self.length*10 - self.pos[j][i])/10
						#	self.canvas.move(cars[j],vel3,0)
						#	self.canvas.update()
						self.canvas.delete(cars[j])
						self.canvas.create_rectangle(-10,50,0,60, fill=color[col[j]], tags=cars[j]) # using j instead of ind(0)
						self.canvas.update()
						time.sleep(0.005)
						veloc = (self.pos[j][i+1]+10)/6.0
						self.canvas.move(cars[j],veloc,0)
						self.canvas.update()
					else:
						time.sleep(0.005)
						veloc = (self.pos[j][i+1]+10)/6.0
						self.canvas.move(cars[j],veloc,0)
						self.canvas.update()
		self.canvas.update()
	#print self.pos


    def reset(self):
	print 'this also does nothing'


#######################################################################################

app = App(root)
#app.__dict__.keys()
#print vars(app).keys()

#print app.maxvel
root.mainloop()