import hashlib
import time

class Block:
    def __init__(self, index, data, previous_hash):
        self.index = index                      # Unique identifier (block number)
        self.timestamp = time.time()            # Timestamp for uniqueness
        self.data = data                        # User input or transaction data
        self.previous_hash = previous_hash      # Hash of the previous block
        self.hash = self.compute_hash()         # Current block's hash

    def compute_hash(self):
        block_contents = f"{self.index}{self.timestamp}{self.data}{self.previous_hash}"
        return hashlib.sha256(block_contents.encode()).hexdigest()

class Blockchain:
    def __init__(self):
        self.chain = []
        self.create_genesis_block()

    def create_genesis_block(self):
        # First block, index 0, dummy data, previous hash of '0'
        genesis_block = Block(0, "Genesis Block", "0")
        self.chain.append(genesis_block)

    def add_block(self, data):
        previous_block = self.chain[-1]
        new_index = previous_block.index + 1
        new_block = Block(new_index, data, previous_block.hash)
        self.chain.append(new_block)

    def display_chain(self):
        for block in self.chain:
            print(f"Block #{block.index}")
            print(f"Timestamp: {block.timestamp}")
            print(f"Data: {block.data}")
            print(f"Hash: {block.hash}")
            print(f"Previous Hash: {block.previous_hash}\n")

    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            curr = self.chain[i]
            prev = self.chain[i - 1]

            if curr.hash != curr.compute_hash():
                return False, f"Block #{curr.index} hash mismatch."
            if curr.previous_hash != prev.hash:
                return False, f"Block #{curr.index} not properly linked to previous block."
        return True, "Blockchain is valid."

# Example usage:
if __name__ == "__main__":
    my_blockchain = Blockchain()

    while True:
        print("\nOptions:")
        print("1. Add new block")
        print("2. Display blockchain")
        print("3. Validate blockchain")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            data = input("Enter block data: ")
            my_blockchain.add_block(data)
            print("Block added.")
        elif choice == "2":
            my_blockchain.display_chain()
        elif choice == "3":
            valid, message = my_blockchain.is_chain_valid()
            print(message)
        elif choice == "4":
            break
        else:
            print("Invalid choice. Try again.")
