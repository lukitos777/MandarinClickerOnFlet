import flet
import asyncio


async def main(page: flet.page) -> None:
    page.title = 'Mandarin Clicker'
    page.theme_mode = flet.ThemeMode.DARK
    page.bgcolor = '#141221'
    page.vertical_aligment = flet.MainAxisAlignment.CENTER
    page.horizontal_aligment = flet.CrossAxisAlignment.CENTER

    async def score_up(event: flet.ContainerTapEvent) -> None:
        score.data += 1
        score.value = str(score.data)
        image.scale = 0.95
        score_counter.opacity = 50
        score_counter.value = '+1'
        score_counter.right = 0
        score_counter.left = event.local_x
        score_counter.top = event.local_y
        score_counter.bottom = 0
        progress_bar.value += (1 / 100)
        if score.data % 100 == 0:
            page.snack_bar = flet.SnackBar(
                content=flet.Text(
                    value='🍊 + 100',
                    size=20,
                    color='#ff8b1f',
                    text_align=flet.TextAlign.CENTER
                ),
                bgcolor='#25223a'
            )
            page.snack_bar.open = True
            progress_bar.value = 0
        await page.update_async()
        await asyncio.sleep(0.1)
        image.scale = 1
        score_counter.opacity = 0
        await page.update_async()

    score = flet.Text(value='0', size=100, data=0, text_align=flet.TextAlign.CENTER)
    score_counter = flet.Text(
        size=50, animate_opacity=flet.Animation(duration=100, curve=flet.AnimationCurve.BOUNCE_IN)
    )
    image = flet.Image(
        src='assets/mandarin.png',
        fit=flet.ImageFit.CONTAIN,
        animate_scale=flet.Animation(duration=600, curve=flet.AnimationCurve.EASE)
    )
    progress_bar = flet.ProgressBar(
        value=0,
        width=page.width - 100,
        bar_height=20,
        color='#ff8b1f',
        bgcolor='#bf6524'
    )

    await page.add_async(
        flet.Container(content=score),
        flet.Container(
            content=flet.Stack(controls=[image, score_counter]),
            on_click=score_up,
            margin=flet.Margin(0, 0, 0, 30)
        ),
        flet.Container(
            content=progress_bar,
            border_radius=flet.BorderRadius(10, 10, 10, 10)
        )
    )


if __name__ == '__main__':
    flet.app(target=main, view=flet.WEB_BROWSER)