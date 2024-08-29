# Generated by Django 5.0 on 2024-08-29 00:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='image',
            field=models.CharField(default='data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAQUAAADBCAMAAADxRlW1AAAAM1BMVEXHx8f////ExMT7+/vLy8vk5OTKysrQ0ND4+Pjv7+/19fXY2NjR0dHU1NTh4eHs7Ozc3Nx6CK3DAAAELklEQVR4nO2c65arIAyFJd5rW+f9n3YERBMLXjqdtuD+fsxyzuBZuA1JCGmzDAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAPB5KLsW9OlJfJxSKdVXn57FR6E6H0RQeewqEGV1XRA9ZdT0o4wIr57Um6GsNC9TNX2XHRaCSpWCJdBNMcqDXo56K0Jh/6suVh8pRDBe7sCTjCIoK0KnVKwyqAfK3U8yiaDvoLu+jHJl2KkvyOt9OjgRzHD7y0+UtkAXjwpK3fc8jBPhaga3x8zoq6i8IgzeYftxqLVDb8NQKhp92Zq74lOiCKiwLYMTQftDuprLixWhjc43BFXYMm63HIwInXUn9unbPYb0XYRVWA96zqtqb+iua/MH7WiiM4Y8LMPabbUdor2os4qbUc142+I9c38ZbnUfXBMutOjry2wV7pc3Tf5lePOFbWNwCWc5BgfnTRt2HRMrjiGcNTxakImRVb69lL6TQNpkuARVWI5s9D8WowgR7iXWlkSwZlAvR1a62DJex5k/riyJkK/vFuOGjcQkQhulCGvGEFBhLC9NDG9/zB5XVtG3E04ZdtpCT5MIzVtn/kKWb3Zmt1/oy9hFWAkTwSVOAfOJuvoY2l4HSyZUesdHLYLbEy5pVhydV4TYtg8LAq7hFrSFPjlL0ATCZSALTFSEoDV4ZfDuQy9vn/J/QHXjk8HjIL0hJc7aswe6z/FvvnrcV04i5M4mmjLCimsIyro+N0/XsVC4lGG2hJqK7l6WP/Vzx7zfy/A8hf7BMwK5R2yYCOaG1CQQsDjAZCjmpXJN+eknmAyugkZMhAhLKU/BYoGVgVh17iwiPMhA9RlFyOZ40FSy2yOZ7GAfNiLovJCLsOtEOyW0DC3JbWec5dW/UOVWBLbNiO/M5e/UPckt5xlFMD0ZECGT9bU4TxteABch2tOGv8ILS2mUUp6Ai2DOZHd2ASYFr67pQ5ohZJ4qezbw6pour5q84XQycBGKKYM82TaC11kLtpc41UaCV6Vrdjp/pq1ExY9kdX2Nt0CdRAZeXRvP6sSR1CkyaRItCmNUEIdSJ5CBuQAeE8SxVPJbCvlZKhYYzySDFEGGRR43kt5WyKaOZTTgMkTcxrSFPMR/DIk8dqTQtOBFiuCJBKJzOlEZZFeL1wFKGVL8sL3sXvNHAZJ99OkVHPaIsMwmkju9lm1b4SKjDKWJySBFWAuDiw7JlOousndtPRdIVgbZu7YVAhetgcmUn+Tb3cwDZEiN/as4JoTj39HSLGRI5riGt/vvygF4WE2mEskc3sHvXxgWRCoisHcb7IV/uMPJEPlnAgTjSj8Q9mxw3fvdHZFAt8vB2K/Da/lv8/kUVBz9qqJrQp3gAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAfAu/nicXLLGOQm8AAAAASUVORK5CYII=', max_length=500),
        ),
    ]
