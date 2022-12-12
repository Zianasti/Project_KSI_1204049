from django import forms

class classform(forms.Form):

    nama = forms.CharField(
        max_length=20, 
        label="Nama Lengkap",
        widget=forms.TextInput(
            attrs={
                'class' : 'form-control',
                'placeholder' : 'Masukkan Nama Lengkap',
            }
        )
        )

    JENIS_KELAMIN = (
        ('P', 'Perempuan'),
        ('L', 'Laki-Laki')
    )

    gender = forms.ChoiceField(
        widget=forms.RadioSelect,
        choices=JENIS_KELAMIN)
    
    TAHUN = range(1945,2018,1)
    tanggal_lahir = forms.DateField (
        widget = forms.SelectDateWidget(years=TAHUN)
    )

    email = forms.EmailField(label="Alamat Email")

    alamat = forms.CharField(
        widget=forms.Textarea,
        max_length=100, 
        required=False)
    agree = forms.BooleanField()

    # python data type
    # nama = forms.CharField(max_length=20)
    # integer_field = forms.IntegerField(required=False)
    # decimal_field = forms.DecimalField()
    # float_field = forms.FloatField()
    # boolean_field = forms.BooleanField()

    # string input
    # email_field = forms.EmailField()
    # slug_field = forms.SlugField()
    # url_field = forms.URLField()
    # ip_field = forms.GenericIPAddressField

    # select input
    # PILIHAN = (
    #     ('nilai1', 'Pilihan1'),
    #     ('nilai2', 'Pilihan2'),
    #     ('nilai3', 'Pilihan3'),
    #     )
    # choice_field = forms.ChoiceField(choices=PILIHAN)
    # multi_choice_field = forms.MultipleChoiceField(choices=PILIHAN)
    # multi_typed_choice = forms.TypedMultipleChoiceField(choices=PILIHAN)

    # date time
    # date_field = forms.DateField()
    # datetime_field = forms.DateTimeField()
    # duration_field = forms.DurationField()
    # time_field = forms.TimeField()
    # splitdatetime_field = forms.SplitDateTimeField()

    # file input
    # image_field = forms.ImageField()
    # file_field = forms.FileField()
    