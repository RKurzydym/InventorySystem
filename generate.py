import asyncio
from prisma import Prisma
import os
Folders = ["No Name","No Name","SMD Stuff","Platienen","Werkzeug zum Schneiden","Schraubendreher","Löt Stuff","No Name","No Name","Werkzeug zum Greifen", "Kabel und Zubehör","Laborzeug","Werkzeug zum festen Halten","Imbus and CO.","Random Stuff","Advanced Geräte"]





async def generate() -> None:
    prisma = Prisma()
    await prisma.connect()
    if(await prisma.inventory.find_unique(where={'name': 'E-Werkstatt'})):
        print('Inventory already exists')
    else:
        # write your queries here
        Inventory = await prisma.inventory.create(
            data={
                'name': 'E-Werkstatt',
                'drawers': {
                    'create': {
                        'name': 'Left Drawer',
                        'folders': {
                                'create': [
                                    {
                                    'name': Folders[0],
                                    'subFolders': {
                                        'create': {
                                            'name': Folders[0],
                                        },
                                    },
                                },
                                {
                                    'name': Folders[1],
                                    'subFolders': {
                                        'create': {
                                            'name': Folders[1],
                                        },
                                    },
                                },
                                {
                                    'name': Folders[2],
                                    'subFolders': {
                                        'create': {
                                            'name': Folders[2],
                                        },
                                    },
                                },
                                {
                                    'name': Folders[3],
                                    'subFolders': {
                                        'create': {
                                            'name': Folders[3],
                                        },
                                    },
                                },
                                ]
                            },
                        
                    },
                },
            },
        )
        
        await prisma.inventory.update(
            where={'name': 'E-Werkstatt'},
            data={
                    'name': 'E-Werkstatt',
                    'drawers': {
                        'create': {
                            'name': 'Center Left Drawer',
                            'folders': {
                                'create': [
                                    {
                                    'name': Folders[4],
                                    'subFolders': {
                                        'create': {
                                            'name': Folders[4],
                                        },
                                    },
                                },
                                {
                                    'name': Folders[5],
                                    'subFolders': {
                                        'create': {
                                            'name': Folders[5],
                                        },
                                    },
                                },
                                {
                                    'name': Folders[6],
                                    'subFolders': {
                                        'create': {
                                            'name': Folders[6],
                                        },
                                    },
                                },
                                {
                                    'name': Folders[7],
                                    'subFolders': {
                                        'create': {
                                            'name': Folders[7],
                                        },
                                    },
                                },
                                {
                                    'name': Folders[8],
                                    'subFolders': {
                                        'create': {
                                            'name': Folders[8],
                                        },
                                    },
                                },
                                ]
                            },
                        
                        },
                    },
            },
        ),
        await prisma.inventory.update(
            where={'name': 'E-Werkstatt'},
            data={
                    'name': 'E-Werkstatt',
                    'drawers': {
                        'create': {
                            'name': 'Center Right Drawer',
                            'folders': {
                                'create': [
                                    {
                                    'name': Folders[9],
                                    'subFolders': {
                                        'create': {
                                            'name': Folders[9],
                                        },
                                    },
                                },
                                {
                                    'name': Folders[10],
                                    'subFolders': {
                                        'create': {
                                            'name': Folders[10],
                                        },
                                    },
                                },
                                {
                                    'name': Folders[11],
                                    'subFolders': {
                                        'create': {
                                            'name': Folders[11],
                                        },
                                    },
                                },
                                {
                                    'name': Folders[12],
                                    'subFolders': {
                                        'create': {
                                            'name': Folders[12],
                                        },
                                    },
                                },
                                ]
                            },
                        },
                    },
            },
        ),
        await prisma.inventory.update(
            where={'name': 'E-Werkstatt'},
            data={
                    'name': 'E-Werkstatt',
                    'drawers': {
                        'create': {
                            'name': 'Right Drawer',
                            'folders': {
                                'create': [
                                    {
                                    'name': Folders[13],
                                    'subFolders': {
                                        'create': {
                                            'name': Folders[13],
                                        },
                                    },
                                },
                                {
                                    'name': Folders[14],
                                    'subFolders': {
                                        'create': {
                                            'name': Folders[14],
                                        },
                                    },
                                },
                                {
                                    'name': Folders[15],
                                    'subFolders': {
                                        'create': {
                                            'name': Folders[15],
                                        },
                                    },
                                },
                                ]
                            },
                        },
                    },
            },
        ),
        

    await prisma.disconnect()

