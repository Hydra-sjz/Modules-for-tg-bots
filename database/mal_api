from jikanpy import AioJikan

async def get_anime_list(name):
    titles = []
    id_list = []
    animelist = AioJikan()
    anime = await animelist.search("anime", name)
    if anime:
        results = anime["results"]
        if results:
            for result in results:
                titles.append(result["title"])
                id_list.append(result["mal_id"])
            await animelist.close()
            return titles, id_list
        else:
            await animelist.close()
            return None, None

async def get_anime_by_id(id, mode="msg"):
    animelist = AioJikan()
    anime = await animelist.anime(id)
    if anime:
        img_url = anime["image_url"]

        title = anime["title"]
        eng_title = anime["title_english"]

        msg = f"<b>Title :</b> <code>{title}</code>\n\n"
        if eng_title and eng_title != title:
            msg += f"<b>Known as :</b> <code>{anime['title_english']}</code>\n\n"
        msg += f"<b>Type :</b> <code>{anime['type']}</code>\n\n"
        msg += f"<b>Episodes :</b> <code>{anime['episodes']}</code>\n\n"
        msg += f"<b>Status :</b> <code>{anime['status']}</code>\n\n"

        short_desc = f"Type: {anime['type']} Status: {anime['status']}"
        try:
            msg += f"<b>Score :</b> <code>{anime['score']}</code>\n\n"
        except:
            pass
        try:
            msg += f"<b>Source :</b> <code>{anime['source']}</code>\n\n"
        except:
            pass
        try:
            msg += f"<b>Aired :</b> <code>{anime['aired']['string']}</code>\n\n"
        except:
            pass
        try:
            desc = anime["synopsis"]
            if len(desc) > 700:
                desc = desc[:700] + "..."
            msg += f"<b>Description :</b>\n<code>{desc}</code>\n\n"
        except:
            pass
        await animelist.close()
        if mode == "msg":
            try:
                trailer = anime["trailer_url"]
            except:
                trailer = None
            return img_url, msg, trailer
        else:
            return img_url, msg, title, short_desc
