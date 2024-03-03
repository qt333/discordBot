import discord
from discord.ext import commands

intents = discord.Intents.all()
intents.members = True

bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')


@bot.event
async def on_member_join(member):
    # Get the specific role by name
    role_name = "рандом"
    role = discord.utils.get(member.guild.roles, name=role_name)

    if role:
        # Add the specified role to the new member
        await member.add_roles(role)

        # Send a welcome message
        welcome_channel_id = 586349140628471811  # Replace with your channel ID
        welcome_channel = member.guild.get_channel(welcome_channel_id)

        if welcome_channel:
            await welcome_channel.send(f"Дарова бродяга, {member.mention}! пока что выступаешь в роле '{role_name}a'")
        else:
            print(f"Error: Welcome channel with ID {welcome_channel_id} not found.")
    else:
        print(f"Error: Role '{role_name}' not found in the server.")

@bot.command()
async def addrole(ctx, member: discord.Member, role: discord.Role):
    """Adds a specified role to the given user."""
    try:
        await member.add_roles(role)
        await ctx.send(f"Role '{role.name}' added to {member.display_name}.")
    except discord.Forbidden:
        await ctx.send("I don't have permission to add roles.")
    except discord.HTTPException as e:
        await ctx.send(f"An error occurred: {e}")
    # await discord.guild.member.add_roles(1213834520332345384)

@bot.command()
async def delrole(ctx, member: discord.Member, role: discord.Role):
    """Adds a specified role to the given user."""
    try:
        await member.remove_roles(role)
        await ctx.send(f"Role '{role.name}' del from {member.display_name}.")
    except discord.Forbidden:
        await ctx.send("I don't have permission to add roles.")
    except discord.HTTPException as e:
        await ctx.send(f"An error occurred: {e}")


@bot.command()
async def createvoice(ctx, role: discord.Role, channel_name: str):
    """Creates a voice channel for a specific role."""
    try:
        # Create overwrites to allow only the specified role to view the channel
        overwrites = {
            ctx.guild.default_role: discord.PermissionOverwrite(view_channel=False),
            role: discord.PermissionOverwrite(view_channel=True)
        }

        # Create the voice channel
        await ctx.guild.create_voice_channel(
            name=channel_name,
            overwrites=overwrites,
            reason=f'Voice channel creation for {role.name}',
        )

        await ctx.send(f"Voice channel '{channel_name}' created for role {role.name}.")
    except discord.Forbidden:
        await ctx.send("I don't have permission to create voice channels.")
    except discord.HTTPException as e:
        await ctx.send(f"An error occurred: {e}")


@bot.command()
async def createtext(ctx, role: discord.Role, channel_name: str):
    """Creates a voice channel for a specific role."""
    try:
        # Create overwrites to allow only the specified role to view the channel
        overwrites = {
            ctx.guild.default_role: discord.PermissionOverwrite(view_channel=False),
            role: discord.PermissionOverwrite(view_channel=True)
        }

        # Create the voice channel
        await ctx.guild.create_text_channel(
            name=channel_name,
            overwrites=overwrites,
            reason=f'Voice channel creation for {role.name}',
        )

        await ctx.send(f"text channel '{channel_name}' created for role {role.name}.")
    except discord.Forbidden:
        await ctx.send("I don't have permission to create text channels.")
    except discord.HTTPException as e:
        await ctx.send(f"An error occurred: {e}")

bot.run('MTIxMzgxMzUxMDcxNTM0Mjk3Mg.GPGNcA.9tCV2955Tr_f44W2RRj7jWNIIDu_GdMs3Vt_A8')

