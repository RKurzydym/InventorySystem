import asyncio
import os
from prisma import Prisma
from prisma.models import Inventory, Drawer, Folder, SubFolder, Item
import generate
from flask import Flask, jsonify


async def main() -> None:
    #Generate the Database if not exists
    await generate.generate()
    #await addItem()
    

async def addItem() -> None:
    #Add a new entry to the database
    
    prisma = Prisma()
    await prisma.connect()
    subFolder = input("Enter the ID of the subfolder: ")
    #print(subFolder)
    findSubfolder = await prisma.subfolder.find_unique(where={'id': int(subFolder)})
    print(findSubfolder.name)
    whatItem = input("What item do you want to add? ")
    amount = input("How many items do you want to add? ")
    operation = await prisma.subfolder.update(
        where={
            'id': int(subFolder)
            },
        data={
            'items':{
                    'create':{
                        'name': whatItem,
                        'amount': int(amount)
                    }
            }
        }
        )


    
"""
if __name__ == '__main__':
    asyncio.run(main())
    """
app = Flask(__name__)

    
@app.route('/')
def index():
    asyncio.run(main())
    data = Inventory.prisma()
    return jsonify(data)
