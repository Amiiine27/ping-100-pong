import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ProjetS4Component } from './projet-s4.component';

describe('ProjetS4Component', () => {
  let component: ProjetS4Component;
  let fixture: ComponentFixture<ProjetS4Component>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [ProjetS4Component]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(ProjetS4Component);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
