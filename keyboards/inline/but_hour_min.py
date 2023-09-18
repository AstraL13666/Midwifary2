from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardButton


# Вместо 93 строк, 15 =)
def but_hour_min():
    work_time = [f"{f'0{hour}' if hour <= 9 else hour}:{min}" for hour in range(6, 20)
                 for min in ("00", "15", "30", "45")]

    b = InlineKeyboardBuilder()

    for time in work_time:
        b.row(
            InlineKeyboardButton(
                text=time,
                callback_data=f"button_{time}"
            )
        )

    b.adjust(4)
    return b.as_markup()
