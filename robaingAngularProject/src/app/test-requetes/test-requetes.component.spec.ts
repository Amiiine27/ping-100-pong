import { ComponentFixture, TestBed } from '@angular/core/testing';

import { TestRequetesComponent } from './test-requetes.component';

describe('TestRequetesComponent', () => {
  let component: TestRequetesComponent;
  let fixture: ComponentFixture<TestRequetesComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [TestRequetesComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(TestRequetesComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
