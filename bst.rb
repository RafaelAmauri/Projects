class Node
	
	def initialize(value)
		@value = value
		@left = @right = nil
	end

	def get_value()
		return @value
	end
 
	def right=(new)
		@right = new
	end	

	def left=(new)
		@left = new
	end

	def right
		return @right
	end
	
	def left
		return @left
	end

end

class BST
	
	def initialize
		@root = nil
	end

	def root
		return @root
	end
	
	def insert(number)
		if @root == nil
			@root = Node.new(number)
			return
		end
		
		search_node = @root
		flag = true

		while(flag) do
			if number < search_node.get_value()
				if search_node.left == nil
					flag = false
					search_node.left = Node.new(number)
				end
	
				search_node = search_node.left		

			else
				if search_node.right == nil	
					flag = false
					search_node.right = Node.new(number)
				end
				
				search_node = search_node.right
			end		

		end
		
	end

	def show(node)
		if not node.left == nil
			show(node.left)
		end

		puts node.get_value()
		
		if not node.right == nil
			show(node.right)
		end
	end	

end


my_bst = BST.new()

my_bst.insert(1)
my_bst.insert(2)
my_bst.insert(-1)

puts "Root = #{my_bst.root.get_value()}"

my_bst.show(my_bst.root)
