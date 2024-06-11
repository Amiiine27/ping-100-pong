import { ComponentFixture, TestBed } from '@angular/core/testing';

import { SupprimerTournoiComponent } from './supprimer-tournoi.component';

describe('SupprimerTournoiComponent', () => {
  let component: SupprimerTournoiComponent;
  let fixture: ComponentFixture<SupprimerTournoiComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [SupprimerTournoiComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(SupprimerTournoiComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
