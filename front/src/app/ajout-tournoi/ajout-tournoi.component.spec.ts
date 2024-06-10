import { ComponentFixture, TestBed } from '@angular/core/testing';

import { AjoutTournoiComponent } from './ajout-tournoi.component';

describe('AjoutTournoiComponent', () => {
  let component: AjoutTournoiComponent;
  let fixture: ComponentFixture<AjoutTournoiComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [AjoutTournoiComponent]
    });
    fixture = TestBed.createComponent(AjoutTournoiComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
