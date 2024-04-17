import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, FormArray, Validators, AbstractControl } from '@angular/forms';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit {
  form: FormGroup;
  expansao: FormArray;

  constructor(private formBuilder: FormBuilder) {}

  ngOnInit() {
    this.form = this.formBuilder.group({
      release_name: ['test', Validators.required],
      expansao: this.formBuilder.array([
        this.createExpansaoFormGroup('test', 'OPEN'),
        this.createExpansaoFormGroup('test2', 'OPEN')
      ])
    });

    this.expansao = this.form.get('expansao') as FormArray;
  }

  createExpansaoFormGroup(flavor: string, status: string): FormGroup {
    return this.formBuilder.group({
      flavor: [flavor, [Validators.required, this.uniqueFlavorValidator()]],
      status: [status, Validators.required]
    });
  }

  addExpansao() {
    const newExpansao = this.createExpansaoFormGroup('', '');
    this.expansao.push(newExpansao);
  }

  removeExpansao(index: number) {
    this.expansao.removeAt(index);
  }

  submitForm() {
    if (this.form.valid) {
      const formData = this.form.value;
      console.log(formData); // Aqui você pode enviar os dados para onde for necessário
    }
  }

  uniqueFlavorValidator() {
    return (control: AbstractControl) => {
      const flavor = control.value;
      const existingFlavors = this.expansao.controls
        .map((item: FormGroup) => item.get('flavor').value)
        .filter((value: string) => value !== control.value);

      return existingFlavors.includes(flavor) ? { duplicateFlavor: true } : null;
    };
  }
}