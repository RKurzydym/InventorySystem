import asyncio
import os
import generate


async def main() -> None:
    #Generate the Database if not exists
    await generate.generate()
    



if __name__ == '__main__':
    asyncio.run(main())