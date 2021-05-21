

class DLinkedNode(): 
	"""
	Node class for doubly linked list
	"""
    def __init__(self):
        self.key = 0
        self.value = 0
        self.prev = None
        self.next = None
            
class CABdata():
    def __init__(self):
    	"""
		A data structure which contains hashmap to keep track of keys and values in the doubly linkedlist with head, middle and tail pointer
    	"""
        self.data_dict = {}
        self.size = 0
        self.head, self.middle, self.tail = DLinkedNode(), DLinkedNode(), DLinkedNode()


        self.head.next = self.middle
        self.middle.prev = self.head

        self.middle.next = self.tail
        self.tail.prev = self.middle


    def _add_node_idle(self, node):
        """
        Always add idle node right after head.
        """
        node.prev = self.head
        node.next = self.head.next

        self.head.next.prev = node
        self.head.next = node

    def _add_node_busy(self, node):
        """
        Always add busy node right after middle.
        """
        node.prev = self.middle
        node.next = self.middle.next

        self.middle.next.prev = node
        self.middle.next = node


    def _remove_node(self, node):
        """
        Remove an existing node from the linked list.
        """
        prev = node.prev
        new = node.next

        prev.next = new
        new.prev = prev



    def _move_busy_to_idle(self, node, cabhistory):
        """
        Remove node from the busy part of linkedlist and add right after head.
        """
        cabhistory.append("IDLE")
        node.value.state = "IDLE"
        self._remove_node(node)
        self._add_node_idle(node)

    def _pop_idle_node(self):
        """
        Pop the idle node just left to middle as it is most idle node and use it for cab.
        """
        res = self.middle.prev
        if res == head:
        	return -1
        self._remove_node(res)
        return res.value

        

    def _pop_busy_node(self, key, cabhistory):
        """
		Pop and move node from busy to idle section of linkedlist
        """
        node = self.data_dict.get(key, None)
        if not node:
            return -1

        self._move_busy_to_idle(node, cabhistory)

        return node.value

    def put_data(self, key, value, states):
        """
		Insert data into the linked list
        """
        newNode = DLinkedNode()
        newNode.key = key
        newNode.value = value

        self.data_dict[key] = newNode
        if states = "IDLE":
        	self._add_node_idle(newNode)
        else:
        	self._add_node_busy(newNode)


        self.size += 1






class Cab():
	"""
	Cab class
	"""
	def __init__(self,cab_id,cab_state,city_id):
		self.cab_id = cab_id
		self.state = cab_state
		self.city_id = city_id
		self.cab_busy_time = []




class City():
	"""
	City class
	"""
	def __init__(self,city_name,city_id):
		self.city_name = None
		self.city_id = None


class CabBookingAdmin():
	"""
	Admin class
	"""

	def onboard_cities(self,city_name,city_id):
		cityobj = City(city_name,city_id)
		return cityobj

	def register_cab(self,cab_id,cab_state,city_id):
		cabobj = Cab(cab_id,cab_state,city_id)
		return cabobj




class CabBookingTool():
	"""
	Booking Tool Class
	"""
	def __init__(self):
		self.city_dict = {}
		self.city_cabs = {}
		self.admin = CabBookingAdmin()
		self.cabhistory = {}

	def addcities(self,city_id,city_name):
		"""
		Method to add cities in the dictionary
		"""
		addedcity = self.admin.onboard_cities(city_name,city_id)
		self.city_dict[city_name] = addedcity
		self.city_cabs[city_id] = CABdata()

	def addcabs(self,cab_id,cab_state,city_id):
		"""
		Method to add cabs in the cities
		"""
		addedcab = self.admin.register_cab(cab_id,cab_state,city_id,[])
		self.cabhistory[cab_id] = []
		self.city_cabs[city_id].put_data(cab_id,addedcab,cab_state)
		self.cabhistory[cab_id].append(cab_state)

	def bookcab(self, start_city, end_city):
		"""
		Method to book cab by customer and return the cabtrip object

		"""
		city_cabs_object_start = self.city_cabs[self.city_dict[start_city].city_id]
		city_cabs_object_end = self.city_cabs[self.city_dict[end_city].city_id]

		res = city_cabs_object_start._pop_idle_node()
		if res == -1:
			print("No cabs available")
			return None
		else:
			addedcabtrip = self.admin.register_cab(res.cab_id,"ON_TRIP",self.city_dict[end_city])
			city_cabs_object_end.put_data(res.cab_id, addedcab,"ON_TRIP")	
			self.cabhistory.append("ON_TRIP")
			return addedcabtrip

	def endtrip(self, cabtrip, end_city):
		"""
		Method to end the trip by customer
		"""
		end_city_id = self.city_dict[end_city].city_id
		cab_id = cabtrip.cab_id
		city_cabs_object_end = self.city_cabs[end_city_id]
		city_cabs_object_end._pop_busy_node(cab_id,cabhistory)
		return "Success"


	def cabhistory(self,cab_id):
		"""
		Return the cab history of a particular cab
		"""
		return self.cabhistory[cab_id]


	



#unknown_city
#unknown_city_id


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)