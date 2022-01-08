from django.test import TestCase
from ...models import Members, Jobs

class MembersModelTests(TestCase):
    # testDBなるものが本物とは別に作成される
    def test_is_empty(self):
        """初期状態では何も登録されていないことをチェック"""  
        saved_member = Members.objects.all()
        self.assertEqual(saved_member.count(), 0)
    
    def test_is_count_one(self):
        """1つレコードを適当に作成すると、レコードが1つだけカウントされることをテスト"""
        # 1つレコードを適当に作成
        # DB毎回ロールバックされるため、jobレコード作成しないとjob.id=1のレコード存在しないでエラーになる
        job = Jobs(
            job_name='writer',
            average_salary=10000,
            is_holiday_on_weekend=True,
            paid_holiday_count=100
        )
        # 一度DBに入れないとレコードとならないため、memberで使えない
        job.save()
        member = Members(
            gender='M',
            username='takashi',
            age='45',
            introduction='Yo',
            # 上で作成したjobオブジェクトを利用
            job = job
        )
        # レコードをDBに保存
        member.save()
        # Jobテーブルの全レコード取得
        saved_member = Members.objects.all()
        # 全レコード合計: 1を確認
        self.assertEqual(saved_member.count(), 1)
    
    def test_saving_and_retrieving_jobs(self):
        """内容を指定してデータを保存し、すぐに取り出した時に保存した時と同じ値が返されることをテスト"""
        job = Jobs(
            job_name='writer',
            average_salary=10000,
            is_holiday_on_weekend=True,
            paid_holiday_count=100
        )
        # 一度DBに入れないとレコードとならないため、memberで使えない
        job.save()
        member = Members(
            gender='M',
            username='takashi',
            age='45',
            introduction='Yo',
            # 上で作成したjobオブジェクトを利用
            job = job
        )
        member.save()
        # 保存したばかりのJobテーブルのレコード取得
        saved_member = Members.objects.first()
        # 保存したjobを取得したものと保存前のjobを比較
        self.assertEqual(saved_member, member)