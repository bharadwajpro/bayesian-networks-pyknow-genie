from pyknow import *

count=0

class SuggestRestuarant(KnowledgeEngine):


	@Rule(NOT(Fact(serve=W())))
	def ask_serve(self):
		self.declare(Fact(serve=input("What kind of service do you need? (sit-down, buffet, fastfood)")))

	@Rule(NOT(Fact(type=W())))
	def ask_type(self):
		self.declare(Fact(type=input("What type of food do you prefer? (vegetarian, non-vegetarian, north-indian, south-indian, international)")))

	@Rule(NOT(Fact(cost=W())))
	def ask_cost(self):
		self.declare(Fact(cost=input("What should the cost be? (cheap, medium, expensive)")))

	@Rule(NOT(Fact(music=W())))
	def ask_music(self):
		self.declare(Fact(music=input("Do you want Music played? (yes, no)")))

	@Rule(NOT(Fact(discount=W())))
	def ask_discount(self):
		self.declare(Fact(discount=input("Is there BITSian Discount? (yes, no)")))


	# @Rule(Fact(serve=MATCH.serve), Fact(type=MATCH.type), Fact(cost=MATCH.cost), AND(OR(Fact(serve='sit-down') , Fact(serve='fastfood') , Fact(serve="")) , OR(Fact(type='vegetarian') , Fact(type='non-vegetarian') , Fact(type='international') , Fact(type="")) , OR(Fact(cost='medium') , Fact(cost=""))))
	@Rule(Fact(serve=MATCH.serve), Fact(type=MATCH.type), Fact(cost=MATCH.cost), Fact(music=MATCH.music), Fact(discount=MATCH.discount), AND(OR(Fact(serve='sit-down') , Fact(serve='fastfood') , Fact(serve="")) , OR(Fact(type='vegetarian') , Fact(type='non-vegetarian') , Fact(type='international') , Fact(type="")) , OR(Fact(cost='medium') , Fact(cost="")) , OR(Fact(music='yes') , Fact(music="")) , OR(Fact(discount='no') , Fact(discount=""))))
	def bits_n_bytes(self):
		global count
		count+=1
		print("Bits-n-Bytes is our recommendation !!")

	# @Rule(Fact(serve=MATCH.serve), Fact(type=MATCH.type), Fact(cost=MATCH.cost), AND(OR(Fact(serve='buffet') , Fact(serve="")) , OR(Fact(type='vegetarian') , Fact(type='non-vegetarian') , Fact(type='north-indian') , Fact(type='south-indian') , Fact(type="")) , OR(Fact(cost='medium') , Fact(cost=""))))
	@Rule(Fact(serve=MATCH.serve), Fact(type=MATCH.type), Fact(cost=MATCH.cost), Fact(music=MATCH.music), Fact(discount=MATCH.discount), AND(OR(Fact(serve='buffet') , Fact(serve="")) , OR(Fact(type='vegetarian') , Fact(type='non-vegetarian') , Fact(type='north-indian') , Fact(type='south-indian') , Fact(type="")) , OR(Fact(cost='medium') , Fact(cost="")) , OR(Fact(music='no') , Fact(music="")) , OR(Fact(discount='no') , Fact(discount=""))))
	def mess1(self):
		global count
		count+=1
		print("Mess-1 is our recommendation !!")

	# @Rule(Fact(serve=MATCH.serve), Fact(type=MATCH.type), Fact(cost=MATCH.cost), AND(OR(Fact(serve='buffet') , Fact(serve="")) , OR(Fact(type='vegetarian') , Fact(type='non-vegetarian') , Fact(type='north-indian') , Fact(type='south-indian') , Fact(type="")) , OR(Fact(cost='medium') , Fact(cost=""))))
	@Rule(Fact(serve=MATCH.serve), Fact(type=MATCH.type), Fact(cost=MATCH.cost), Fact(music=MATCH.music), Fact(discount=MATCH.discount), AND(OR(Fact(serve='buffet') , Fact(serve="")) , OR(Fact(type='vegetarian') , Fact(type='non-vegetarian') , Fact(type='north-indian') , Fact(type='south-indian') , Fact(type="")) , OR(Fact(cost='medium') , Fact(cost="")) , OR(Fact(music='no') , Fact(music="")) , OR(Fact(discount='no') , Fact(discount=""))))
	def mess2(self):
		global count
		count+=1
		print("Mess-2 is our recommendation !!")

	# @Rule(Fact(serve=MATCH.serve), Fact(type=MATCH.type), Fact(cost=MATCH.cost), AND(OR(Fact(serve='sit-down') , Fact(serve='fastfood') , Fact(serve="")) , OR(Fact(type='vegetarian') , Fact(type='non-vegetarian') , Fact(type='maggie') , Fact(type=""))))
	@Rule(Fact(serve=MATCH.serve), Fact(type=MATCH.type), Fact(cost=MATCH.cost), Fact(music=MATCH.music), Fact(discount=MATCH.discount), AND(OR(Fact(serve='sit-down') , Fact(serve='fastfood') , Fact(serve="")) , OR(Fact(type='vegetarian') , Fact(type='non-vegetarian') , Fact(type='maggie') , Fact(type="")) , OR(Fact(cost='cheap') , Fact(cost="")) , OR(Fact(music='no') , Fact(music="")) , OR(Fact(discount='no') , Fact(discount=""))))
	def yummpys(self):
		global count
		count+=1
		print("Yummpys is our recommendation !!")

	# @Rule(Fact(serve=MATCH.serve), Fact(type=MATCH.type), Fact(cost=MATCH.cost), AND(OR(Fact(serve='sit-down') , Fact(serve='fastfood') , Fact(serve="")) , OR(Fact(type='vegetarian') , Fact(type='non-vegetarian') , Fact(type='north-indian') , Fact(type='south-indian') , Fact(type="")) , OR(Fact(cost='expensive') , Fact(cost=""))))
	@Rule(Fact(serve=MATCH.serve), Fact(type=MATCH.type), Fact(cost=MATCH.cost), Fact(music=MATCH.music), Fact(discount=MATCH.discount), AND(OR(Fact(serve='sit-down') , Fact(serve='fastfood') , Fact(serve="")) , OR(Fact(type='vegetarian') , Fact(type='non-vegetarian') , Fact(type='north-indian') , Fact(type='south-indian') , Fact(type="")) , OR(Fact(cost='expensive') , Fact(cost="")) , OR(Fact(music='no') , Fact(music="")) , OR(Fact(discount='no') , Fact(discount=""))))
	def c3(self):
		global count
		count+=1
		print("Chai Coffee Company is our recommendation !!")

	# @Rule(Fact(serve=MATCH.serve), Fact(type=MATCH.type), Fact(cost=MATCH.cost), AND(OR(Fact(serve='sit-down') , Fact(serve="")) , OR(Fact(type='vegetarian') , Fact(type='non-vegetarian') , Fact(type='north-indian') , Fact(type='south-indian') , Fact(type='international') , Fact(type="")) , OR(Fact(cost='expensive') , Fact(cost=""))))
	@Rule(Fact(serve=MATCH.serve), Fact(type=MATCH.type), Fact(cost=MATCH.cost), Fact(music=MATCH.music), Fact(discount=MATCH.discount), AND(OR(Fact(serve='sit-down') , Fact(serve="")) , OR(Fact(type='vegetarian') , Fact(type='non-vegetarian') , Fact(type='north-indian') , Fact(type='south-indian') , Fact(type='international') , Fact(type="")) , OR(Fact(cost='expensive') , Fact(cost="")) , OR(Fact(music='yes') , Fact(music="")) , OR(Fact(discount='yes') , Fact(discount=""))))
	def alankrita(self):
		global count
		count+=1
		print("Alankrita is our recommendation !!")

	# @Rule(Fact(serve=MATCH.serve), Fact(type=MATCH.type), Fact(cost=MATCH.cost), AND(OR(Fact(serve='sit-down') , Fact(serve="")) , OR(Fact(type='vegetarian') , Fact(type='non-vegetarian') , Fact(type="")) , OR(Fact(cost='medium') , Fact(cost=""))))
	@Rule(Fact(serve=MATCH.serve), Fact(type=MATCH.type), Fact(cost=MATCH.cost), Fact(music=MATCH.music), Fact(discount=MATCH.discount), AND(OR(Fact(serve='sit-down') , Fact(serve="")) , OR(Fact(type='vegetarian') , Fact(type='non-vegetarian') , Fact(type="")) , OR(Fact(cost='medium') , Fact(cost="")) , OR(Fact(music='no') , Fact(music="")) , OR(Fact(discount='yes') , Fact(discount=""))))
	def viceroy(self):
		global count
		count+=1
		print("Viceroy is our recommendation !!")


engine = SuggestRestuarant()
engine.reset()
engine.run()

if count==0:
	print("Sorry!! We cannot recommend any restaurants nearby")